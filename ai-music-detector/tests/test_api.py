import io
import wave

import numpy as np
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def wav_bytes(samples: np.ndarray, sr: int = 16000) -> bytes:
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((samples * 32767).astype("<i2").tobytes())
    return buf.getvalue()


def post(data: bytes):
    return client.post("/api/analyze", files={"audio": ("rec.wav", data, "audio/wav")})


def test_analyze_returns_probability():
    t = np.arange(16000 * 8) / 16000
    rng = np.random.default_rng(0)
    sig = 0.3 * np.sin(2 * np.pi * 440 * t) + 0.05 * rng.standard_normal(len(t))
    res = post(wav_bytes(sig))
    assert res.status_code == 200
    assert 0 <= res.json()["ai_probability"] <= 1


def test_too_short_rejected():
    res = post(wav_bytes(0.3 * np.sin(np.arange(16000) / 10)))
    assert res.status_code == 400


def test_silence_rejected():
    res = post(wav_bytes(np.zeros(16000 * 8)))
    assert res.status_code == 400


def test_invalid_file_rejected():
    assert post(b"not a wav").status_code == 400
