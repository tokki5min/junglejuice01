---
name: action-live-director
description: 실사(라이브액션) 액션 영상 프롬프트를 설계·수리하는 액션 연출 전문 스킬. 격투·총격·검술·카체이스·추격·스턴트·와이어 액션을 실제로 촬영한 영화처럼 보이게 만든다. Seedance 2.5/2.0 중심이고 Kling·Veo·MiniMax H3·Wan에도 적용한다. 8대 액션 연출 그룹(시간·충격·힘 전달·움직임·카메라·시각효과·편집·여운), 매치 온 액션, 스턴트 안무 문법, 실사 고정(PHOTOREAL LOCK)을 담는다. "실사 액션", "액션 영화처럼", "격투 장면", "총격전", "카체이스", "스턴트", "홍콩 액션", "존 윅 스타일", "타격감", "맞는 느낌이 없어", "액션이 따로 놀아", "매치 온 액션", "실사인데 애니처럼 나와" 같은 요청이나, 사람이 실제로 싸우는 사진풍 영상 프롬프트를 짜거나 고칠 때 반드시 사용한다. 애니메이션·2D 액션은 action-anime-director, 최종 문장 규칙은 seedance-clean, 인물 실사감은 photoreal과 연계한다.
---

# Action Live Director

실사 액션의 타격감은 효과가 아니라 **몸이 받는 힘**에서 나온다. 애니가 선(스미어·임팩트 프레임)으로 과장한다면, 실사는 **체중 이동·카메라 반응·여운**으로 무게를 증명한다.

사용자는 한국어로 소통한다. 설명은 한국어, 프롬프트는 영어.

## 0. 먼저 읽을 것

| 상황 | 읽을 파일 |
|---|---|
| 타격 하나를 설계할 때 | `references/action-impact-taxonomy.md` (8대 그룹, 실사 열 사용) |
| 샷을 나눠 동작을 이을 때 | `references/match-on-action.md` |
| 실사 액션 문구가 필요할 때 | `references/live-phrasebook.md` |
| 결과물이 이상할 때 | 아래 §6 진단표, 그다음 `references/live-lessons.md` |

## 1. 작업 순서

1. **싸움의 논리.** "습관 → 미끼 → 역전"처럼 전술을 한 줄로 정한다. 실사는 특히 **환경 활용**(벽, 문, 테이블, 계단, 자동차)이 설득력을 만든다.
2. **타격 설계.** 핵심 타격마다 KINETIC(체중 이동) + CAMERA(렌즈 반응) + AFTERMATH(여운)를 기본으로 겹친다. TEMPORAL(스피드 램프), IMPACT(플래시), VISUAL(노출 스파이크)은 씬당 1~2회만 쓴다.
3. **컷 설계.** 실사 AI는 긴 컷에서 손가락, 얼굴, 몸의 형태가 무너진다. 그래서 **3초 안팎의 짧은 샷**을 매치 온 액션으로 잇는다. 방향, 속도, 동작 단계를 맞춘다.
4. **실사 고정(PHOTOREAL LOCK)** 을 맨 앞과 LOCKS에 둔다(§3).
5. **4,000자 이내.** 줄일 때는 배경 묘사부터 줄인다.
6. 생성 후 §6 진단표로 고친다. 한 번에 문장 하나만 고친다.

## 2. 프롬프트 골격

```
TITLE / 21:9, 12s, timed multishot. Cuts only at the marked points, the camera does not cut on its own.

PHOTOREAL LOCK   Live-action footage shot on a full-frame cinema camera with spherical primes, 24 fps, 180-degree shutter.
                 Real performers and stunt doubles, practical sets, practical dust and debris captured in camera.
REFERENCE        @image1: the lead. 100% matches the reference. References bind appearance, not framing or poses.
LOGLINE          전술 역전 한 줄 + 샷 수.
RULES            무기 개수와 소유, 탄약 수, 화면 축(누가 화면 왼쪽인지), 환경 소품.
LOCATION         전경, 중경, 배경 / 광원 / 동선.
0.0s to 3.0s — SHOT 1, [shot size], [angle], [FOV°], [camera rig: handheld / Steadicam / dolly / car mount]
  카메라 → 동작 → 접촉 → 힘의 결과 → 여운
3.0s MATCH CUT ON ACTION — [동작]이 [단계]에서 [방향]으로 진행 중
...
PERFORMANCE      피부 질감, 땀, 숨, 근육 긴장, 눈빛.
LIGHTING         광원, 방향, 색온도(K).
AUDIO            주먹 타격음, 옷 스치는 소리, 숨소리, 공간 잔향. 음악 유무를 명시한다.
OUTPUT           real-time vs slow-motion per shot, fine film grain.
LOCKS            무기, 인원, 부상과 의상 상태의 연속성, 실사 고정을 다시 한 번.
```

## 3. 실사 고정 — 애니처럼 나오는 것을 막는다

- 형용사(`photorealistic`, `cinematic`) 대신 **촬영 조건**을 적는다: 카메라, 렌즈, 셔터, 실제 배우, 실제 세트, 실물 효과(practical effects).
- 액션은 판타지 쪽으로 끌려가기 쉽다. 그래서 불가능한 동작은 **와이어와 스턴트로 촬영한 것**으로 적는다: `The leap is a wire-assisted stunt captured in camera.`
- **애니 단어를 쓰지 않는다.** `smear`, `sakuga`, `speed lines`, `impact frame`, `squash and stretch`, `cel`, `ink`, `anime`, `stylized`, `dreamlike`는 결과물을 애니로 끌고 간다. 대체 표현은 아래와 같다.

| 애니 표현 | 실사 대체 |
|---|---|
| smear frame | `natural motion blur from a 180-degree shutter` |
| impact frame | `a single white flash frame` / `the frame shakes once` |
| speed lines | `streaking background blur on the whip pan` |
| squash on landing | `knees absorb the landing, body compresses, then drives up` |
| hit-stop | `a sharp speed ramp into 20% for the contact, snapping back to real time` |

- **사람의 질감:** 땀방울, 모공, 붉어진 피부, 흐트러진 잔머리, 근육이 떨리는 모습, 거친 숨. 옷은 무게를 가지고 반 박자 늦게 따라온다.

## 4. 실사 액션 핵심 규칙

**힘 전달 (KINETIC)이 전부다**
- 타격은 **맞는 쪽의 몸**으로 판다(sell the hit): `The punch lands and his head snaps sideways, weight dropping onto his back heel, knees buckling.`
- 때리는 쪽도 반작용을 받는다: `her shoulder recoils from the impact, she resets her stance`.
- 순서를 적는다: 시작 → 접촉 → 체중 이동 → 넘어짐 → 여운 (`Show the hit, THEN the fall.`).
- 스턴트 문법을 쓴다: `fight choreography with clear reach and timing`, `reaction shot sells the hit`, `breakfall onto the mat`, `a stunt double takes the fall through the table`.

**카메라**
- 핸드헬드는 **진동 폭을 수치로** 준다: `handheld with 1-2 cm tremor`. 충격이 오면 한 번 꺾였다가 바로 안정된다: `jolts once on impact and settles`.
- 휩팬은 0.8초 이상으로 준다. 더 짧으면 블러 없는 하드컷처럼 보인다.
- 원테이크 롱테이크는 "보이지 않는 컷"으로 설계한다. 다만 길어질수록 몸이 무너지니, 12초 이하로 쓰거나 매치 온 액션으로 나눈다.
- FOV는 각도 숫자로 적는다: 격투 근접 24~35mm 상당(63~84°), 반응샷 50~85mm 상당(29~47°).
- 매 샷 앵글을 바꾼다: 로우, 어깨 너머, 측면 트래킹, 탑다운. 정면 고정은 피한다.

**편집 (EDITORIAL)**
- **Cut on impact:** 접촉하는 순간 반응 각도로 컷한다.
- **Match on action:** 방향, 속도, 동작 단계를 맞춘다(`references/match-on-action.md`).
- **오버래핑 액션(홍콩 액션식):** 같은 타격을 두 각도에서 한 번씩, 총 두 번 보여 준다. 씬당 한 번만 쓴다. `The same kick lands twice from two angles: first wide, then a tight reverse.`

**총격·차량·무기**
- 총격은 발마다 따로 적는다: 섬광 1회, 탄피 1개, 반동 1회. 탄약 수를 센다: `Each shot has one muzzle flash, one ejected casing and visible recoil; 7 rounds, then the slide locks open.`
- 차량은 무게와 관성을 적는다: 서스펜션 눌림, 타이어 미끄러짐, 유리 파편.
- 무기 회계: 개수, 누가 쥐는지, 떨어뜨린 위치까지 적는다. 매 샷 손 상태를 다시 쓴다.

**연속성**
- 부상, 땀, 피, 찢어진 옷은 **누적된다.** 씬 사이에서 리셋하지 않는다.
- 화면 축을 고정한다: `She stays screen-left, he stays screen-right in every shared view.`

## 5. 수위

- 피는 소량으로 사실적으로 적는다: `a thin cut on the cheekbone`, `a split lip`. 과도한 고어나 노출은 필터에 걸린다.
- 가림은 사물, 앵글, 그림자, 연기로 한다. 노출을 단어로 지시하지 않는다.

## 6. 결과 진단표

| 증상 | 원인 | 한 문장 수정 |
|---|---|---|
| 애니·게임 CG처럼 나옴 | 애니 단어, 판타지 전제 | 촬영 조건으로 실사 고정 + 애니 단어 제거 |
| 때려도 가벼움 | 맞는 쪽 반응이 없음 | 머리가 꺾이고 체중이 무너지는 과정 + 카메라 저크 + 여운 |
| 액션이 따로 놂 / 몸이 녹아내림 | 한 컷이 너무 김 | 3초 샷으로 매치 온 액션 분할 |
| 컷이 바뀌면 동작이 반복되거나 튐 | 동작 단계 불일치 | `End mid-X` / `Start mid-X` 지점 일치 |
| 컷 후 동작이 반대로 보임 | 화면 방향 불일치 | `still travelling screen-right` + 축 고정 |
| 둥둥 떠 있음 | 와이어 질감 없음, 슬로모션 남용 | 착지 무게, 실시간 기본, 슬로모션은 별도 샷으로 |
| 총이 연사로 뭉개짐 | 발별로 묘사하지 않음 | 발마다 섬광·탄피·반동 1회씩 + 총 발수 |
| 손가락·무기가 녹음 | 근접 손 클로즈업이 김 | 손 인서트는 짧게, 와이드로 복귀 |
| 얼굴이 바뀜 | 긴 샷, 측면 프로필 | 레퍼런스 각도를 추가 + 짧은 샷 |

## 7. 성장 규칙

- 사용자가 결과를 피드백하면 `references/live-lessons.md`에 **증상 → 원인 → 수정 문장**으로 한 줄씩 추가한다.
- 자매 스킬 `action-anime-director`와 taxonomy·match-on-action을 공유한다. 한쪽을 고치면 다른 쪽에도 반영한다.
- 새 연구 자료(사용자가 공유하는 글, 영상 분석)는 출처와 함께 phrasebook에 추가한다.
