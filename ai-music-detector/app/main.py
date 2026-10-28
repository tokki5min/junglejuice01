import io
import wave
from pathlib import Path

import numpy as np
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .detector import SAMPLE_RATE, Detector, HeuristicDetector

STATIC = Path(__file__).parent / "static"
MAX_BYTES = 10 * 1024 * 1024

app = FastAPI(title="AI 음악 판독기")
detector: Detector = HeuristicDetector()


def read_wav(data: bytes) -> tuple[np.ndarray, int]:
    try:
        with wave.open(io.BytesIO(data)) as w:
            if w.getsampwidth() != 2:
                raise ValueError("16-bit PCM WAV만 지원합니다.")
            sr, ch = w.getframerate(), w.getnchannels()
            pcm = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2")
    except (wave.Error, EOFError) as e:
        raise ValueError("WAV 파일을 읽을 수 없습니다.") from e
    samples = pcm.astype(np.float32) / 32768.0
    if ch > 1:
        samples = samples.reshape(-1, ch).mean(axis=1)
    return samples, sr


@app.post("/api/analyze")
async def analyze(audio: UploadFile = File(...)):
    data = await audio.read()
    if len(data) > MAX_BYTES:
        raise HTTPException(413, "파일이 너무 큽니다.")
    try:
        samples, sr = read_wav(data)
        result = detector.predict(samples, sr)
    except ValueError as e:
        raise HTTPException(400, str(e))
    return {
        "ai_probability": result.ai_probability,
        "confidence": result.confidence,
        "features": result.features,
        "note": result.note,
    }


@app.get("/")
def index():
    return FileResponse(STATIC / "index.html")


app.mount("/static", StaticFiles(directory=STATIC), name="static")
