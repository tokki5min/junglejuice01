# AI 음악 판독기

카페 등에서 흘러나오는 음악을 폰 마이크로 12초 듣고 AI 생성 가능성을 바로 보여주는 웹앱.

## 실행
```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
폰에서 마이크를 쓰려면 HTTPS가 필요합니다. 로컬 테스트는 `localhost`에서만 되고,
폰에서는 `cloudflared tunnel --url http://localhost:8000` 같은 터널로 접속하세요.

## 현재 상태
- 판독기(`app/detector.py`)는 스펙트럼 통계 기반 **실험용 규칙**입니다. 학습된 모델이 아니며 정확도는 검증되지 않았습니다.
- `Detector` 인터페이스를 구현해 학습된 모델로 교체할 수 있습니다.

## 다음 단계
1. AI/사람 곡 데이터셋 확보 후 분류 모델 학습 (카페 소음·스피커 왜곡 증강 포함)
2. 곡 식별 API(ACRCloud 등)와 결합해 알려진 곡 여부로 보정
