# 매치 온 액션 (Match on Action)

샷이 바뀌어도 동작은 이어진다. 하나의 동작을 서로 다른 각도의 샷으로 이어 붙이는 편집 기법이다.

출처: Threads @byulmiso의 AI 액션 연출 글. AI 생성에 맞게 다시 정리했다.

## 왜 AI 영상에 특히 중요한가
- AI 영상은 컷이 길어질수록 동작이 늘어지고 몸의 형태가 흔들린다.
- 동작을 여러 샷으로 쪼개고 각 샷의 좋은 구간만 이어 붙이면, 긴 컷에서 드러나는 어색함이 줄어든다.
- 관객의 시선은 계속되는 움직임을 따라간다. 그래서 샷이 바뀌어도 하나의 행동으로 받아들인다.

## 반드시 맞출 세 가지
1. **방향:** 첫 샷에서 주먹이 화면 오른쪽으로 나갔다면 다음 샷도 오른쪽으로 이어진다. 갑자기 왼쪽으로 가면 움직임이 뒤집힌 것처럼 느껴진다. 이를 지키려면 카메라를 동작 축의 같은 편에 둔다.
2. **속도:** 빠르게 뻗던 주먹이 다음 샷에서 느려지면 힘과 리듬이 끊긴다. 각도가 바뀌어도 같은 기세를 유지한다.
3. **동작 단계:** 첫 샷에서 팔이 절반쯤 뻗었다면 다음 샷도 그 지점에서 시작한다. 팔을 다시 당기면 동작이 반복되어 보이고, 이미 다 뻗은 상태에서 시작하면 중간이 빠져 보인다.

## 생성 단계에서 설계하는 법
샷을 처음부터 쪼개서 설계한다. 하나는 **"뻗기 시작하는 샷"**, 다른 하나는 **"계속 뻗어 나가 타격하는 샷"**이다.

**한 프롬프트 안의 멀티샷일 때:**
```
2.0s MATCH CUT ON ACTION — the punch is half-extended and still travelling screen-right at the cut.
2.0s to 4.0s — SHOT 2, low side angle. The same punch continues from the half-extended point at the same speed, still travelling screen-right, and lands on his jaw.
```

**따로 생성해서 편집으로 붙일 때:**
- 샷 A 프롬프트 끝 문장: `End mid-punch: the fist is half-extended, moving screen-right at full speed.`
- 샷 B 프롬프트 첫 문장: `Start mid-punch: the fist is already half-extended, moving screen-right at full speed, and continues into the impact.`
- 편집할 때 A의 마지막 몇 프레임과 B의 처음 몇 프레임을 겹쳐 보고, 동작이 가장 자연스럽게 맞는 프레임을 골라 자른다.
- 두 샷 모두 넉넉하게(앞뒤 0.5초 이상) 생성해 두면 편집할 여유가 생긴다.

## 점검표
- [ ] 컷 직전과 직후, 동작 방향이 같은가 (화면 기준 왼쪽/오른쪽)
- [ ] 속도가 같은가 (한쪽만 슬로모션이 아닌가)
- [ ] 동작 단계가 이어지는가 (반복되거나 건너뛰지 않는가)
- [ ] 카메라가 동작 축을 넘지 않았는가 (넘으려면 보이는 오빗으로 넘는다)

## 의도적 예외
음악 비트에 맞춰 **일부러 방향을 뒤집는** 매치 온 액션은 묘한 쾌감을 준다. 규칙을 아는 상태에서 비트 위에서만, 한 씬에 한 번만 쓴다.
`On the heavy beat, MATCH CUT ON ACTION with a deliberate screen-direction flip: the spin continues from the reverse side.`
