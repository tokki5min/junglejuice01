"""AI 음악 판독기.

`Detector`를 구현하면 학습된 모델로 교체할 수 있다.
기본 `HeuristicDetector`는 스펙트럼 통계만 보는 실험용 구현이며,
카페 마이크 녹음처럼 잡음이 큰 입력에서는 정확도를 보장하지 않는다.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

import numpy as np

SAMPLE_RATE = 16000
MIN_SECONDS = 5


@dataclass
class Result:
    ai_probability: float  # 0.0 ~ 1.0
    confidence: str  # "low" | "medium"
    features: dict[str, float] = field(default_factory=dict)
    note: str = ""


class Detector(Protocol):
    def predict(self, samples: np.ndarray, sample_rate: int) -> Result: ...


def _spectrum_features(samples: np.ndarray, sr: int) -> dict[str, float]:
    frame, hop = 2048, 1024
    n = (len(samples) - frame) // hop + 1
    window = np.hanning(frame)
    mags = np.stack(
        [np.abs(np.fft.rfft(samples[i * hop : i * hop + frame] * window)) for i in range(n)]
    )
    power = mags**2 + 1e-12
    freqs = np.fft.rfftfreq(frame, 1 / sr)

    flatness = np.exp(np.mean(np.log(power), axis=1)) / np.mean(power, axis=1)
    mean_spec = power.mean(axis=0)
    cum = np.cumsum(mean_spec) / mean_spec.sum()
    rolloff = float(freqs[np.searchsorted(cum, 0.95)])

    flux = np.sqrt(np.sum(np.diff(mags, axis=0) ** 2, axis=1))
    flux_cv = float(flux.std() / (flux.mean() + 1e-12))

    rms = np.sqrt(np.mean(samples**2))
    return {
        "spectral_flatness": float(flatness.mean()),
        "rolloff_95_hz": rolloff,
        "flux_variation": flux_cv,
        "rms": float(rms),
    }


class HeuristicDetector:
    """실험용 규칙 기반 점수. 학습된 모델이 아니므로 참고용으로만 쓴다."""

    def predict(self, samples: np.ndarray, sample_rate: int) -> Result:
        if len(samples) < MIN_SECONDS * sample_rate:
            raise ValueError(f"최소 {MIN_SECONDS}초 이상 녹음이 필요합니다.")
        feats = _spectrum_features(samples, sample_rate)
        if feats["rms"] < 0.005:
            raise ValueError("소리가 거의 들리지 않습니다. 스피커 쪽으로 폰을 가까이 대 주세요.")

        # 생성 음악은 프레임 간 변화(flux)가 규칙적인 경향이 있어 변동계수가 낮다.
        regularity = float(np.clip((1.2 - feats["flux_variation"]) / 0.8, 0, 1))
        smooth = float(np.clip(1 - feats["spectral_flatness"] * 20, 0, 1))
        score = 0.65 * regularity + 0.35 * smooth
        return Result(
            ai_probability=round(float(np.clip(score, 0.05, 0.95)), 3),
            confidence="low",
            features={k: round(v, 4) for k, v in feats.items()},
            note="실험용 규칙 기반 점수입니다. 학습된 모델 연결 전까지 참고용으로만 보세요.",
        )
