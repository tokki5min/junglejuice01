---
name: action-anime-director
description: 2D 애니메이션 액션 영상(무협·검술·격투·추격·초능력 배틀) 프롬프트를 설계·수리하는 액션 연출 전문 스킬. Seedance 2.5/2.0 중심, MiniMax H3·Wan·Kling에도 적용. Kōda(@aimikoda)의 공개 프롬프트 연구와 실제 제작 세션의 실패·수정 기록을 합쳐 만든 규칙집이다. "액션 씬", "싸움 장면", "검술", "무협", "전투", "추격전", "타격감", "속도감", "사쿠가", "임팩트 프레임", "칼이 다시 손에 생겨", "화살이 멈춰 보여", "구도가 밋밋해", "프레임 브레이크", "코다 스타일" 같은 요청이나, 애니풍 액션 영상 프롬프트를 새로 짜거나 고칠 때 반드시 사용한다. 최종 문장 규칙은 seedance-clean, 12원칙 모션 블록은 anime-motion-style, 캐릭터 정지 이미지는 midjourney-v8-compiler와 연계한다.
---

# Action Anime Director

액션은 형용사가 아니라 **원인 → 접촉 → 결과**의 연쇄로 쓴다. 이 스킬은 (1) 액션 안무를 짜는 법, (2) 모델이 잘 무너지는 지점을 미리 막는 고정 규칙, (3) 결과물 진단표를 담는다.

사용자는 한국어로 소통한다. 설명은 한국어, 프롬프트는 영어.

## 0. 먼저 읽을 것

| 상황 | 읽을 파일 |
|---|---|
| 액션 문구가 필요할 때 | `references/koda-phrasebook.md` (검증된 원문 문구 사전) |
| 완성 예시를 보고 싶을 때 | `references/koda-examples.md` |
| 결과물이 이상할 때 | `references/session-lessons.md` (실제 실패 → 수정 기록) |
| 연구 이력/다음 연구 | `references/research-log.md` |

## 1. 작업 순서

1. **싸움의 논리부터.** 장면마다 "습관 → 미끼 → 역전" 같은 전술 한 줄을 정한다. 예: *A가 계속 왼팔 아래로 빠져나가 뒤를 친다 → B가 그 습관을 미끼로 두 번째 칼로 출구를 막는다.* 이게 없으면 그냥 칼 휘두르는 영상이 된다.
2. **분량 예산.** 길이에 비해 내용이 많으면 Seedance 2.5는 장면을 **빨리감기처럼 압축**한다(코다 실측). 3초 = 핵심 동작 1개 + 결과 1개. 30초 = 5~6샷이 적정.
3. **레퍼런스 결속 → 규칙 → 타임라인 → 룩 → 사운드 → 고정** 순서로 쓴다(§2).
4. **4,000자 이내**로 맞춘다(API/MCP 경로 한도). 줄일 땐 배경 묘사부터, 동작·카메라·고정은 마지막까지 남긴다.
5. 생성 후 §5 진단표로 실패 레이어를 찾고 **문장 하나만** 고쳐 재생성한다.

## 2. 프롬프트 골격 (코다식 + 세션 검증)

```
TITLE / 21:9, 12s, timed multishot. Cuts only at the marked points, the camera does not cut on its own.

REFERENCE        @image1: the heroine. 100% matches the reference.  ← 외형 묘사 금지(사용자 규칙)
                 References bind appearance, not framing or poses.
LOGLINE          한 문장: 누가 무엇을, 전술 역전 한 줄, 샷 수.
RULES            무기 개수·소유·손 상태 / 화면 축(누가 화면 왼쪽) / 능력 규칙 / 적 행동 규칙
STYLE            2D 렌더링을 선·채색 단어로 구체화 + 기울어진 수평선·전경 레이어
FRAME RATE       캐릭터 on twos 12fps / 카메라·배경·이펙트 on ones 24fps
0.0s to 3.0s — SHOT 1, [앵글], [기울기], [FOV]; [전경]
  카메라 먼저 → 동작 → 접촉 → 결과(반동·파편·자세)
3.0s HARD CUT
...
AUDIO            디에제틱 효과음만. 음악·대사 필요 없으면 명시적으로 뺀다.
MOTION STYLE     12원칙 압축판 + 이 씬의 "단 하나의 과장 비트"
LOCKS            무기·손·인원 수·의상 상태·씬 간 연속성. 각 1문장.
```

코다는 긴 블록 대신 **밀도 높은 산문 + 타임코드 비트**도 자주 쓴다. 30초 원테이크·몽타주형이면 단락형도 허용.

## 3. 액션 핵심 규칙

**속도**
- 동작 중에 시작하고 동작 중에 끝낸다: `Start immediately in motion.` / `Cut mid-exchange, both still attacking.`
- 기본은 실시간: `Full-speed action throughout. No slow motion, speed ramps, long windups or floating pauses.` 슬로모션·히트스톱은 **세어서 1~2회만** 의도적으로 쓰고, 쓸 땐 그 샷 전체를 한 속도로(샷 중간 전환 금지).
- 속도는 스미어 + 접촉 시 카메라 충격으로: `brief directional smears resolving into clear anatomy at contact`, `Jolt the camera on contact`.
- 연결: `Carry parries into displacement and recoveries into attacks.` 방어가 곧 다음 공격이 된다.

**타격**
- 순서를 적는다: `Show shot, impact, THEN fall.` 결과는 즉시·국소: `Hits have immediate local results; defeated bodies stay down.`
- 이펙트는 절제·접촉 기원: `Sparse thin arcs, silhouette smears and tiny flecks sourced from motion or contact.`
- 힘이 보이게: 상태("조른다")가 아니라 **가해자 동작 + 피해자 반응 + 리듬**으로 쓴다(예: 4자 잠금, 상체 비틀기, `three hard pulses`, 얼굴 붉어짐·핏줄·눈 뒤집힘).

**카메라**
- 카메라를 무기 운동량에 묶는다: `Couple the camera to sword momentum: blade-height whip tracking, violent orbits, close foreground passes and snap zooms.`
- 오빗은 각도·시작·끝을 수치로: `UNBROKEN 60-DEGREE PARTIAL ORBIT ... Finish the curved camera move before cutting.`
- 빠르게 움직이는 물체(화살·볼트)는 **화면을 가로지르게** 잡는다. 카메라 축 방향으로 멀어지면 멈춘 것처럼 보인다. `streaks across the frame at full speed, moving the entire time`.
- 정면 구도 금지 습관: 매 샷 `horizon tilted N degrees` + 전경 레이어 + 오프센터. 앵글은 샷마다 바꾼다(로우·하이·사이드·탑다운·어깨너머).
- 클로즈업은 짧은 인서트, 항상 와이드로 복귀: `close-ups are brief inserts returning wide`.

**연속성 (가장 자주 깨지는 곳)**
- 무기 회계: `Exactly N swords; hilts stay in their owning hands. No dropped, merged, duplicated or floating weapons.`
- 무기를 잃은 뒤에는 **매 샷 손 상태를 다시 쓰고** 무기의 위치를 추적한다: `Both hands empty ... her sword is a tiny glint still spinning high in the sky.`
- 컷마다 모델은 레퍼런스 이미지로 돌아간다 → 레퍼런스에 칼이 있으면 칼이 되살아난다. 이름표도 `swordswoman` 대신 `heroine`. 필요하면 무기 없는 레퍼런스로 교체.
- 화면 축: `She advances LEFT TO RIGHT. All cameras stay on the same side of that axis.`
- 연작이면 씬 간 상태(칼 뽑힘/칼집 버림/옷 손상/날씨)를 표로 관리하고 각 프롬프트 LOCKS에 반영한다. 씬 사이에 의미 없는 리셋(칼집에 넣기 등) 금지.

**스타일 고정**
- "anime" 한 단어 대신 선·채색을 구체적으로: `thin broken ink, rough painterly fills, elastic sketch contours, compact hand-painted shading, flat cel shadows, paper grain`.
- 새로 등장하는 요소에도 스타일을 확장: `Extend this treatment to [new element].`
- 실루엣을 새까맣게 만드는 단어 주의: `solid black silhouette`, `strong black silhouettes`는 몸을 검게 칠한다 → `bold ink outlines`.

**12fps 애니 느낌**
- 캐릭터만 on twos, 카메라·배경·이펙트는 on ones. 전부 12fps로 지시하면 카메라 무빙이 끊겨 저프레임 영상처럼 보인다. 슬로모션 샷은 전부 on ones.

## 4. 특수 기법 레시피

- **프레임 브레이크(팝아웃)**: `COMPOSITING ORDER, BACK TO FRONT: 1. background 2. two black letterbox bars 3. foreground character` + `The foreground character is NOT confined to that window` + 고정 카메라. 바 두께는 모델이 정한다(코다: 퍼센트 지정해도 흔들림). 카메라를 움직이면 바가 휜다.
- **칼 궤적 전환**: `Blade trails mask seamless cuts between shots` / `Her rising arc eclipses the lens.`
- **텔레포트**: 사라진 자리는 비워 두고(`Every disappearance leaves clearly empty space`) 도착은 공격 도중(`She reforms mid-attack`).
- **속도를 부재로 표현**: `the camera catches only fragments, impacts and consequences, while she is already somewhere else.`
- **잔상 되감기 / 충전 후 방출 / 즉발 빔** 문구는 phrasebook 참조.
- **긴 단편 파이프라인(코다)**: 전체 이야기를 30초 480p로 먼저 테스트 → 프레임 캡처로 캐릭터 시트·빈 배경 플레이트 → 3개 프롬프트로 분할 → 깨진 10초만 재생성 → 이전 결과 프레임을 다음 구간 레퍼런스로.

## 5. 결과 진단표

| 증상 | 원인 | 한 문장 수정 |
|---|---|---|
| 빨리감기처럼 보임 | 길이 대비 내용 과다 | 샷당 동작 1개로 줄이거나 길이 늘리기 |
| 둥둥 떠 있음 | 슬로모션·홀드 과다 | `No slow motion, floating pauses` + 접촉 즉시 반동 |
| 타격감 없음 | 접촉 결과 미기술 | `Show impact, THEN recoil` + 카메라 저크 |
| 조르기·잡기에 힘이 없음 | 상태만 기술 | 잠금 방법 + 펄스 리듬 + 상대 얼굴 반응 |
| 잃은 무기가 다시 손에 | 레퍼런스 재참조, `swordswoman`, 위치 미추적 | 매 샷 빈손 명시 + 무기 위치 + 이름표 교체 |
| 화살·투사체가 멈춤 | 깊이축 이동, 망원 | 측면에서 가로지르게, `moving the entire time` |
| 구도가 정면·평면적 | 앵글 미지정 | 기울기·전경·오프센터·앵글 순환 |
| 몸이 새까맘 | silhouette 단어 | `bold ink outlines`, 옅은 먹 그늘 |
| 의상이 덧입혀짐 | 프롬프트에 속옷 기술 / 모델 안전 성향 | 의상은 사용자 설정 그대로, 가림은 사물로 |
| 카메라가 끊겨 보임 | 전체 12fps 지시 | 카메라·배경 on ones 분리 |
| 3D 느낌 | 스타일 단어 추상적 | 선·채색 구체어 + 레퍼런스를 스타일 잠금으로 |

## 6. 금기

- 레퍼런스 인물의 외형 묘사(사용자 규칙: `@image1`만 지정)
- 0.2초 같은 프레임 단위 미세 타이밍(12fps에서 2장 분량이라 무의미)
- 한 샷에 핵심 동작 3개 이상
- 의미 없는 형용사(`epic, cinematic, dynamic`)
- 노출을 단어로 지시(`nude` 등) — 필터 거부. 가림은 사물·머리카락·앵글로.

## 7. 스킬 성장 규칙

- 사용자가 결과 피드백을 줄 때마다 `references/session-lessons.md`에 **증상 → 원인 → 수정 문장**을 한 줄 추가한다.
- 정기 연구: `scripts/koda_scrape.py <out.json> <pages>`로 새 게시물을 수집하고, 새 기법만 phrasebook에 추가, `research-log.md`에 날짜·범위·발견을 기록한다.
- 출처는 연구용 인용으로만 쓰고, 원문 프롬프트를 통째로 재배포하지 않는다.
