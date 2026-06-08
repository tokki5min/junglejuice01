"""Concurrency and polling helpers — the heart of the semi-automated workflow.

The tutorial calls out three automations the code owns: 동시성 (run several jobs
in parallel), 폴링 (poll async jobs until done), 후처리 (post-process). The first
two live here so every stage shares one tested implementation, including the
per-engine concurrency ceiling (e.g. Higgsfield's 8-job limit).
"""

from __future__ import annotations

import asyncio
from typing import Awaitable, Callable, Sequence, TypeVar

T = TypeVar("T")
R = TypeVar("R")


async def map_with_limit(
    items: Sequence[T],
    worker: Callable[[T], Awaitable[R]],
    limit: int,
) -> list[R]:
    """Run `worker` over `items` with at most `limit` coroutines in flight.

    Results are returned in input order. This is the batching primitive the image
    and video stages use to respect each engine's concurrency ceiling instead of
    firing 90 requests at once.
    """

    if limit < 1:
        raise ValueError("limit must be >= 1")

    semaphore = asyncio.Semaphore(limit)

    async def guarded(item: T) -> R:
        async with semaphore:
            return await worker(item)

    return await asyncio.gather(*(guarded(item) for item in items))


async def poll_until(
    check: Callable[[], Awaitable[T | None]],
    *,
    interval: float = 3.0,
    timeout: float = 600.0,
    sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
) -> T:
    """Poll an async job until it returns a non-None result or times out.

    `check` should return the finished result, or None while the job is still
    running. `sleep` is injectable so tests can drive the loop without real waits.
    """

    elapsed = 0.0
    while True:
        result = await check()
        if result is not None:
            return result
        if elapsed >= timeout:
            raise TimeoutError(f"Job did not finish within {timeout}s")
        await sleep(interval)
        elapsed += interval
