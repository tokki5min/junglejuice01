# THE ART OF REAL LIFE K-POP IDOL ENGINE V2.0

## 목적

이 문서는 기존 V1.0 프롬프트를 더 안전하고 다양하게 확장한 독립형 이미지 프롬프트 생성 지침이다. 모든 인물은 실제 아이돌이나 실존 연예인이 아니라 **가상의 성인(21세 이상) K-beauty 패션 모델**로 지정한다.

## Section 0: Operation Logic — Anti-Collage 4 Prompt Generator

### Trigger Words

사용자가 `고`, `go`, `Go`, `GO`, `ㄱ`, `g` 중 하나만 입력하면 실행한다.

### Critical Anti-Collage Rule

- 절대 한 번의 이미지 요청 안에 4장을 만들라고 지시하지 않는다.
- 서로 다른 4개의 완성형 단일 이미지 프롬프트를 만든다.
- 각 프롬프트는 독립된 세로 9:16 사진 1장만 생성하도록 작성한다.
- Job 1은 Image Prompt 1만, Job 2는 Image Prompt 2만, Job 3은 Image Prompt 3만, Job 4는 Image Prompt 4만 실행한다.

### Never Use

- 2x2 grid, collage, contact sheet, split screen, panel layout, quadrants
- four variations in one image, multiple photos in one canvas
- borders, dividing lines, layout grid, combined output

### Required Output Per Job

- one standalone vertical 9:16 photo
- one fictional adult subject
- one scene
- one camera frame
- realistic natural light and K-beauty detail
- no logo, no watermark, no celebrity likeness

## Section 1: Fixed Core Base

Use this exact base in every prompt:

> Ultra-realistic vertical 9:16 candid fashion photo of one fictional adult Korean K-beauty idol-inspired model, age 21+, not a real celebrity, natural skin texture, subtle pores, realistic hair strands, refined K-beauty makeup, tasteful styling, daily-life realism, cinematic natural light, shallow depth of field, high-resolution smartphone/editorial hybrid, single subject, single scene, one camera frame, no collage, no split screen, no grid, no border, no text, no watermark.

## Random Selection Logic

- Section 1 is always fixed.
- Sections 2, 3, 4, 5: randomly select one option each while avoiding options used in the recent 10 generations.
- Sections 6, 7, 8: randomly select one option each while avoiding options used in the recent 20 generations.
- Within the current batch of 4 prompts, avoid duplicate options across all sections as much as possible.
- If all options are exhausted by memory rules, reset the oldest half of the memory list first rather than repeating the most recent options.

## Prompt Assembly Rule

For each of the 4 prompts, combine exactly:

`[Section 1 Fixed Core Base] + [Section 2 Muse Face] + [Section 3 Expression] + [Section 4 Hairstyle] + [Section 5 Body Silhouette] + [Section 6 Styling] + [Section 7 Pose] + [Section 8 Scene]`

Then append:

> Composition: single vertical 9:16 portrait photo, full-body or three-quarter body as appropriate, one person only, one continuous environment, realistic camera perspective, no collage formatting.

## Safety and Realism Guardrails

- The model must always be an adult age 21+.
- Do not imply school-age, teen, underage, childlike, or minor-coded identity.
- Do not request explicit nudity, transparent exposure, sexual acts, fetish framing, or non-consensual framing.
- Swimwear and lingerie-inspired fashion must remain tasteful, fashion/editorial, and non-explicit.
- Avoid copying the face, body, name, stage identity, or signature styling of a real K-pop idol.


## Section 2: Muse Face Bank (100)

1. [Bloom Pure 1] round eyes with subtle aegyo-sal and coral MLBB lips; natural daylight realism
2. [Puppy Innocent 1] deep monolid eyes with soft smoky shadow; soft K-beauty finish
3. [Clear Glassy 1] defined bone structure with natural brows; candid phone-camera warmth
4. [Sharp Monolid 1] warm amber gaze with muted coral lips; editorial-clean balance
5. [Peach Fresh 1] sharp monolid eyes with matte pink lips; natural daylight realism
6. [Feline Grace 1] heavy-lidded eyes with wet glossy lips; soft K-beauty finish
7. [Cool Almond 1] velvet matte lips with quiet gaze; candid phone-camera warmth
8. [Mysterious Mono 1] honey-toned cheeks with soft glossy lips; editorial-clean balance
9. [Serene Luxury 1] almond eyes with satin beige lips; natural daylight realism
10. [Doe Innocent 1] smoky monolid eyes with fine liner; soft K-beauty finish
11. [Gentle Lidded 1] ivory skin glow with soft lashes; candid phone-camera warmth
12. [Tear Natural 1] clear eyes with inner double eyelids and nude glossy lips; editorial-clean balance
13. [Glass Skin Pure 1] wide doe eyes with catchlights and plump gloss; natural daylight realism
14. [Soft Smoke Chic 1] clear brown eyes with apricot blush; soft K-beauty finish
15. [Urban Structure 1] clean chic brows with blurred lip edge; candid phone-camera warmth
16. [Moonlit Calm 1] feline upward eyes with berry gradient lips; editorial-clean balance
17. [Apricot Dew 1] soft round eyes with glass-skin cheeks; natural daylight realism
18. [Velvet Mono 1] neutral latte lips with calm eyebrows; soft K-beauty finish
19. [Crystal Smile 1] droopy puppy eyes with translucent lip gloss; candid phone-camera warmth
20. [Rose Beige 1] poised eyes with defined lashes and beige lips; editorial-clean balance
21. [Ivory Soft 1] gentle eyes with champagne shimmer; natural daylight realism
22. [Amber Glance 1] pearl-like skin with pink beige tint; soft K-beauty finish
23. [Pearl Fresh 1] half-moon smiling eyes with peach tinted lips; candid phone-camera warmth
24. [Quiet Chic 1] natural moist lower lids and softly swollen lips; editorial-clean balance
25. [Honey Glow 1] bright catchlights with soft rose lips; natural daylight realism
26. [Bloom Pure 2] droopy puppy eyes with translucent lip gloss; soft K-beauty finish
27. [Puppy Innocent 2] poised eyes with defined lashes and beige lips; candid phone-camera warmth
28. [Clear Glassy 2] gentle eyes with champagne shimmer; editorial-clean balance
29. [Sharp Monolid 2] pearl-like skin with pink beige tint; natural daylight realism
30. [Peach Fresh 2] half-moon smiling eyes with peach tinted lips; soft K-beauty finish
31. [Feline Grace 2] natural moist lower lids and softly swollen lips; candid phone-camera warmth
32. [Cool Almond 2] bright catchlights with soft rose lips; editorial-clean balance
33. [Mysterious Mono 2] round eyes with subtle aegyo-sal and coral MLBB lips; natural daylight realism
34. [Serene Luxury 2] deep monolid eyes with soft smoky shadow; soft K-beauty finish
35. [Doe Innocent 2] defined bone structure with natural brows; candid phone-camera warmth
36. [Gentle Lidded 2] warm amber gaze with muted coral lips; editorial-clean balance
37. [Tear Natural 2] sharp monolid eyes with matte pink lips; natural daylight realism
38. [Glass Skin Pure 2] heavy-lidded eyes with wet glossy lips; soft K-beauty finish
39. [Soft Smoke Chic 2] velvet matte lips with quiet gaze; candid phone-camera warmth
40. [Urban Structure 2] honey-toned cheeks with soft glossy lips; editorial-clean balance
41. [Moonlit Calm 2] almond eyes with satin beige lips; natural daylight realism
42. [Apricot Dew 2] smoky monolid eyes with fine liner; soft K-beauty finish
43. [Velvet Mono 2] ivory skin glow with soft lashes; candid phone-camera warmth
44. [Crystal Smile 2] clear eyes with inner double eyelids and nude glossy lips; editorial-clean balance
45. [Rose Beige 2] wide doe eyes with catchlights and plump gloss; natural daylight realism
46. [Ivory Soft 2] clear brown eyes with apricot blush; soft K-beauty finish
47. [Amber Glance 2] clean chic brows with blurred lip edge; candid phone-camera warmth
48. [Pearl Fresh 2] feline upward eyes with berry gradient lips; editorial-clean balance
49. [Quiet Chic 2] soft round eyes with glass-skin cheeks; natural daylight realism
50. [Honey Glow 2] neutral latte lips with calm eyebrows; soft K-beauty finish
51. [Bloom Pure 3] clear eyes with inner double eyelids and nude glossy lips; candid phone-camera warmth
52. [Puppy Innocent 3] wide doe eyes with catchlights and plump gloss; editorial-clean balance
53. [Clear Glassy 3] clear brown eyes with apricot blush; natural daylight realism
54. [Sharp Monolid 3] clean chic brows with blurred lip edge; soft K-beauty finish
55. [Peach Fresh 3] feline upward eyes with berry gradient lips; candid phone-camera warmth
56. [Feline Grace 3] soft round eyes with glass-skin cheeks; editorial-clean balance
57. [Cool Almond 3] neutral latte lips with calm eyebrows; natural daylight realism
58. [Mysterious Mono 3] droopy puppy eyes with translucent lip gloss; soft K-beauty finish
59. [Serene Luxury 3] poised eyes with defined lashes and beige lips; candid phone-camera warmth
60. [Doe Innocent 3] gentle eyes with champagne shimmer; editorial-clean balance
61. [Gentle Lidded 3] pearl-like skin with pink beige tint; natural daylight realism
62. [Tear Natural 3] half-moon smiling eyes with peach tinted lips; soft K-beauty finish
63. [Glass Skin Pure 3] natural moist lower lids and softly swollen lips; candid phone-camera warmth
64. [Soft Smoke Chic 3] bright catchlights with soft rose lips; editorial-clean balance
65. [Urban Structure 3] round eyes with subtle aegyo-sal and coral MLBB lips; natural daylight realism
66. [Moonlit Calm 3] deep monolid eyes with soft smoky shadow; soft K-beauty finish
67. [Apricot Dew 3] defined bone structure with natural brows; candid phone-camera warmth
68. [Velvet Mono 3] warm amber gaze with muted coral lips; editorial-clean balance
69. [Crystal Smile 3] sharp monolid eyes with matte pink lips; natural daylight realism
70. [Rose Beige 3] heavy-lidded eyes with wet glossy lips; soft K-beauty finish
71. [Ivory Soft 3] velvet matte lips with quiet gaze; candid phone-camera warmth
72. [Amber Glance 3] honey-toned cheeks with soft glossy lips; editorial-clean balance
73. [Pearl Fresh 3] almond eyes with satin beige lips; natural daylight realism
74. [Quiet Chic 3] smoky monolid eyes with fine liner; soft K-beauty finish
75. [Honey Glow 3] ivory skin glow with soft lashes; candid phone-camera warmth
76. [Bloom Pure 4] sharp monolid eyes with matte pink lips; editorial-clean balance
77. [Puppy Innocent 4] heavy-lidded eyes with wet glossy lips; natural daylight realism
78. [Clear Glassy 4] velvet matte lips with quiet gaze; soft K-beauty finish
79. [Sharp Monolid 4] honey-toned cheeks with soft glossy lips; candid phone-camera warmth
80. [Peach Fresh 4] almond eyes with satin beige lips; editorial-clean balance
81. [Feline Grace 4] smoky monolid eyes with fine liner; natural daylight realism
82. [Cool Almond 4] ivory skin glow with soft lashes; soft K-beauty finish
83. [Mysterious Mono 4] clear eyes with inner double eyelids and nude glossy lips; candid phone-camera warmth
84. [Serene Luxury 4] wide doe eyes with catchlights and plump gloss; editorial-clean balance
85. [Doe Innocent 4] clear brown eyes with apricot blush; natural daylight realism
86. [Gentle Lidded 4] clean chic brows with blurred lip edge; soft K-beauty finish
87. [Tear Natural 4] feline upward eyes with berry gradient lips; candid phone-camera warmth
88. [Glass Skin Pure 4] soft round eyes with glass-skin cheeks; editorial-clean balance
89. [Soft Smoke Chic 4] neutral latte lips with calm eyebrows; natural daylight realism
90. [Urban Structure 4] droopy puppy eyes with translucent lip gloss; soft K-beauty finish
91. [Moonlit Calm 4] poised eyes with defined lashes and beige lips; candid phone-camera warmth
92. [Apricot Dew 4] gentle eyes with champagne shimmer; editorial-clean balance
93. [Velvet Mono 4] pearl-like skin with pink beige tint; natural daylight realism
94. [Crystal Smile 4] half-moon smiling eyes with peach tinted lips; soft K-beauty finish
95. [Rose Beige 4] natural moist lower lids and softly swollen lips; candid phone-camera warmth
96. [Ivory Soft 4] bright catchlights with soft rose lips; editorial-clean balance
97. [Amber Glance 4] round eyes with subtle aegyo-sal and coral MLBB lips; natural daylight realism
98. [Pearl Fresh 4] deep monolid eyes with soft smoky shadow; soft K-beauty finish
99. [Quiet Chic 4] defined bone structure with natural brows; candid phone-camera warmth
100. [Honey Glow 4] warm amber gaze with muted coral lips; editorial-clean balance

## Section 3: Natural Daily Expression Bank (100)

1. [Gentle Smile 1] soft eye crinkles and slightly lifted mouth corners; natural daylight realism
2. [Soft Laugh 1] heavy relaxed eyelids and slightly parted lips; soft K-beauty finish
3. [Bashful Smile 1] heavy eyelids with a soft satisfied smile; candid phone-camera warmth
4. [Curious Tilt 1] light amused head shake with small smile; editorial-clean balance
5. [Direct Eye Contact 1] head tilted with one eyebrow gently raised; natural daylight realism
6. [Relaxed Gaze 1] big genuine smile with slight head tilt back; soft K-beauty finish
7. [Playful Glance 1] soft yawn with half-closed eyes; candid phone-camera warmth
8. [Contented Sigh 1] calm sideways glance; editorial-clean balance
9. [Surprised Blink 1] one-sided smile with mischievous sparkle; natural daylight realism
10. [Thoughtful Pout 1] raised eyebrows and bright forward energy; soft K-beauty finish
11. [Bright Laugh 1] tiny approving nod and kind eyes; candid phone-camera warmth
12. [Shy Side Glance 1] downward gaze with a small bashful smile; editorial-clean balance
13. [Calm Neutral 1] gently pursed lips looking up to the right; natural daylight realism
14. [Excited Spark 1] lower lip gently bitten in concentration; soft K-beauty finish
15. [Tired Content 1] light cheek puff and relaxed happiness; candid phone-camera warmth
16. [Nose Scrunch 1] soft unfocused eyes and fully relaxed face; editorial-clean balance
17. [Lip Bite Focus 1] neutral lips and soft natural stare; natural daylight realism
18. [Easy Yawn 1] far-away gaze with loose facial muscles; soft K-beauty finish
19. [Confident Smile 1] eye-smile lines with a natural upper-teeth laugh; candid phone-camera warmth
20. [Dreamy Soft 1] quick wide eyes with natural open mouth; editorial-clean balance
21. [Subtle Nod 1] light nose wrinkle and happy narrowed eyes; natural daylight realism
22. [Gentle Head Shake 1] sudden blink and parted lips; soft K-beauty finish
23. [Quick Blink Surprise 1] steady camera gaze with slightly widened eyes; candid phone-camera warmth
24. [Cheek Puff 1] sideways eyes with small closed-mouth smile; editorial-clean balance
25. [Casual Side Glance 1] strong eye contact and relaxed smile; natural daylight realism
26. [Gentle Smile 2] eye-smile lines with a natural upper-teeth laugh; soft K-beauty finish
27. [Soft Laugh 2] quick wide eyes with natural open mouth; candid phone-camera warmth
28. [Bashful Smile 2] light nose wrinkle and happy narrowed eyes; editorial-clean balance
29. [Curious Tilt 2] sudden blink and parted lips; natural daylight realism
30. [Direct Eye Contact 2] steady camera gaze with slightly widened eyes; soft K-beauty finish
31. [Relaxed Gaze 2] sideways eyes with small closed-mouth smile; candid phone-camera warmth
32. [Playful Glance 2] strong eye contact and relaxed smile; editorial-clean balance
33. [Contented Sigh 2] soft eye crinkles and slightly lifted mouth corners; natural daylight realism
34. [Surprised Blink 2] heavy relaxed eyelids and slightly parted lips; soft K-beauty finish
35. [Thoughtful Pout 2] heavy eyelids with a soft satisfied smile; candid phone-camera warmth
36. [Bright Laugh 2] light amused head shake with small smile; editorial-clean balance
37. [Shy Side Glance 2] head tilted with one eyebrow gently raised; natural daylight realism
38. [Calm Neutral 2] big genuine smile with slight head tilt back; soft K-beauty finish
39. [Excited Spark 2] soft yawn with half-closed eyes; candid phone-camera warmth
40. [Tired Content 2] calm sideways glance; editorial-clean balance
41. [Nose Scrunch 2] one-sided smile with mischievous sparkle; natural daylight realism
42. [Lip Bite Focus 2] raised eyebrows and bright forward energy; soft K-beauty finish
43. [Easy Yawn 2] tiny approving nod and kind eyes; candid phone-camera warmth
44. [Confident Smile 2] downward gaze with a small bashful smile; editorial-clean balance
45. [Dreamy Soft 2] gently pursed lips looking up to the right; natural daylight realism
46. [Subtle Nod 2] lower lip gently bitten in concentration; soft K-beauty finish
47. [Gentle Head Shake 2] light cheek puff and relaxed happiness; candid phone-camera warmth
48. [Quick Blink Surprise 2] soft unfocused eyes and fully relaxed face; editorial-clean balance
49. [Cheek Puff 2] neutral lips and soft natural stare; natural daylight realism
50. [Casual Side Glance 2] far-away gaze with loose facial muscles; soft K-beauty finish
51. [Gentle Smile 3] downward gaze with a small bashful smile; candid phone-camera warmth
52. [Soft Laugh 3] gently pursed lips looking up to the right; editorial-clean balance
53. [Bashful Smile 3] lower lip gently bitten in concentration; natural daylight realism
54. [Curious Tilt 3] light cheek puff and relaxed happiness; soft K-beauty finish
55. [Direct Eye Contact 3] soft unfocused eyes and fully relaxed face; candid phone-camera warmth
56. [Relaxed Gaze 3] neutral lips and soft natural stare; editorial-clean balance
57. [Playful Glance 3] far-away gaze with loose facial muscles; natural daylight realism
58. [Contented Sigh 3] eye-smile lines with a natural upper-teeth laugh; soft K-beauty finish
59. [Surprised Blink 3] quick wide eyes with natural open mouth; candid phone-camera warmth
60. [Thoughtful Pout 3] light nose wrinkle and happy narrowed eyes; editorial-clean balance
61. [Bright Laugh 3] sudden blink and parted lips; natural daylight realism
62. [Shy Side Glance 3] steady camera gaze with slightly widened eyes; soft K-beauty finish
63. [Calm Neutral 3] sideways eyes with small closed-mouth smile; candid phone-camera warmth
64. [Excited Spark 3] strong eye contact and relaxed smile; editorial-clean balance
65. [Tired Content 3] soft eye crinkles and slightly lifted mouth corners; natural daylight realism
66. [Nose Scrunch 3] heavy relaxed eyelids and slightly parted lips; soft K-beauty finish
67. [Lip Bite Focus 3] heavy eyelids with a soft satisfied smile; candid phone-camera warmth
68. [Easy Yawn 3] light amused head shake with small smile; editorial-clean balance
69. [Confident Smile 3] head tilted with one eyebrow gently raised; natural daylight realism
70. [Dreamy Soft 3] big genuine smile with slight head tilt back; soft K-beauty finish
71. [Subtle Nod 3] soft yawn with half-closed eyes; candid phone-camera warmth
72. [Gentle Head Shake 3] calm sideways glance; editorial-clean balance
73. [Quick Blink Surprise 3] one-sided smile with mischievous sparkle; natural daylight realism
74. [Cheek Puff 3] raised eyebrows and bright forward energy; soft K-beauty finish
75. [Casual Side Glance 3] tiny approving nod and kind eyes; candid phone-camera warmth
76. [Gentle Smile 4] head tilted with one eyebrow gently raised; editorial-clean balance
77. [Soft Laugh 4] big genuine smile with slight head tilt back; natural daylight realism
78. [Bashful Smile 4] soft yawn with half-closed eyes; soft K-beauty finish
79. [Curious Tilt 4] calm sideways glance; candid phone-camera warmth
80. [Direct Eye Contact 4] one-sided smile with mischievous sparkle; editorial-clean balance
81. [Relaxed Gaze 4] raised eyebrows and bright forward energy; natural daylight realism
82. [Playful Glance 4] tiny approving nod and kind eyes; soft K-beauty finish
83. [Contented Sigh 4] downward gaze with a small bashful smile; candid phone-camera warmth
84. [Surprised Blink 4] gently pursed lips looking up to the right; editorial-clean balance
85. [Thoughtful Pout 4] lower lip gently bitten in concentration; natural daylight realism
86. [Bright Laugh 4] light cheek puff and relaxed happiness; soft K-beauty finish
87. [Shy Side Glance 4] soft unfocused eyes and fully relaxed face; candid phone-camera warmth
88. [Calm Neutral 4] neutral lips and soft natural stare; editorial-clean balance
89. [Excited Spark 4] far-away gaze with loose facial muscles; natural daylight realism
90. [Tired Content 4] eye-smile lines with a natural upper-teeth laugh; soft K-beauty finish
91. [Nose Scrunch 4] quick wide eyes with natural open mouth; candid phone-camera warmth
92. [Lip Bite Focus 4] light nose wrinkle and happy narrowed eyes; editorial-clean balance
93. [Easy Yawn 4] sudden blink and parted lips; natural daylight realism
94. [Confident Smile 4] steady camera gaze with slightly widened eyes; soft K-beauty finish
95. [Dreamy Soft 4] sideways eyes with small closed-mouth smile; candid phone-camera warmth
96. [Subtle Nod 4] strong eye contact and relaxed smile; editorial-clean balance
97. [Gentle Head Shake 4] soft eye crinkles and slightly lifted mouth corners; natural daylight realism
98. [Quick Blink Surprise 4] heavy relaxed eyelids and slightly parted lips; soft K-beauty finish
99. [Cheek Puff 4] heavy eyelids with a soft satisfied smile; candid phone-camera warmth
100. [Casual Side Glance 4] light amused head shake with small smile; editorial-clean balance

## Section 4: K-Beauty Hairstyle Bank (100)

1. [Mirror Glass Straight 1] sleek black straight hair with center part and high-gloss strands; natural daylight realism
2. [Natural Long Straight 1] bouncy blow-dried crown volume with soft curves; soft K-beauty finish
3. [Blunt Chin Bob 1] tangled bed hair with realistic friction texture; candid phone-camera warmth
4. [Matte Silk Straight 1] polished sleek low bun; editorial-clean balance
5. [Airy Hush Cut 1] matte smooth straight hair with layered volume; natural daylight realism
6. [Romantic Dry Waves 1] half-up tie with lower waves flowing; soft K-beauty finish
7. [Beach Messy Waves 1] loose low ponytail with falling strands; candid phone-camera warmth
8. [Voluminous Blowout 1] collarbone-length layered lob with airy ends; editorial-clean balance
9. [High Sleek Ponytail 1] irregular rough sea waves with matte salt texture; natural daylight realism
10. [Low Effortless Bun 1] damp post-wash hair with darker roots and clumped ends; soft K-beauty finish
11. [Half-Up Romantic 1] half-up top knot with loose lower hair; candid phone-camera warmth
12. [Messy Fluffy Updo 1] sharp blunt bob at jawline with clean ends; editorial-clean balance
13. [Wind-Swept Layers 1] low loose bun with natural stray hairs; natural daylight realism
14. [Natural Damp Glow 1] straight hair with soft side part; soft K-beauty finish
15. [Candid Disheveled 1] two loose space buns with falling strands; candid phone-camera warmth
16. [Fine Baby Hair Focus 1] thick dry fluffy waves with natural volume; editorial-clean balance
17. [Side Part Straight 1] messy layers sweeping across face; natural daylight realism
18. [Loose Low Ponytail 1] shaggy bob with choppy texture; soft K-beauty finish
19. [Soft Curtain Bangs 1] long straight hair with natural weight and subtle sheen; candid phone-camera warmth
20. [Textured Shaggy Bob 1] high tight ponytail with smooth scalp and dynamic tail; editorial-clean balance
21. [Half-Up Top Knot 1] translucent baby hairs along the hairline; natural daylight realism
22. [Sleek Low Bun 1] soft waves with middle part; soft K-beauty finish
23. [Wavy Middle Part 1] heavily layered hush cut with airy face-framing strands; candid phone-camera warmth
24. [Messy Space Bun 1] loosely pinned updo with protruding strands; editorial-clean balance
25. [Soft Layered Lob 1] long hair with curtain bangs; natural daylight realism
26. [Mirror Glass Straight 2] long straight hair with natural weight and subtle sheen; soft K-beauty finish
27. [Natural Long Straight 2] high tight ponytail with smooth scalp and dynamic tail; candid phone-camera warmth
28. [Blunt Chin Bob 2] translucent baby hairs along the hairline; editorial-clean balance
29. [Matte Silk Straight 2] soft waves with middle part; natural daylight realism
30. [Airy Hush Cut 2] heavily layered hush cut with airy face-framing strands; soft K-beauty finish
31. [Romantic Dry Waves 2] loosely pinned updo with protruding strands; candid phone-camera warmth
32. [Beach Messy Waves 2] long hair with curtain bangs; editorial-clean balance
33. [Voluminous Blowout 2] sleek black straight hair with center part and high-gloss strands; natural daylight realism
34. [High Sleek Ponytail 2] bouncy blow-dried crown volume with soft curves; soft K-beauty finish
35. [Low Effortless Bun 2] tangled bed hair with realistic friction texture; candid phone-camera warmth
36. [Half-Up Romantic 2] polished sleek low bun; editorial-clean balance
37. [Messy Fluffy Updo 2] matte smooth straight hair with layered volume; natural daylight realism
38. [Wind-Swept Layers 2] half-up tie with lower waves flowing; soft K-beauty finish
39. [Natural Damp Glow 2] loose low ponytail with falling strands; candid phone-camera warmth
40. [Candid Disheveled 2] collarbone-length layered lob with airy ends; editorial-clean balance
41. [Fine Baby Hair Focus 2] irregular rough sea waves with matte salt texture; natural daylight realism
42. [Side Part Straight 2] damp post-wash hair with darker roots and clumped ends; soft K-beauty finish
43. [Loose Low Ponytail 2] half-up top knot with loose lower hair; candid phone-camera warmth
44. [Soft Curtain Bangs 2] sharp blunt bob at jawline with clean ends; editorial-clean balance
45. [Textured Shaggy Bob 2] low loose bun with natural stray hairs; natural daylight realism
46. [Half-Up Top Knot 2] straight hair with soft side part; soft K-beauty finish
47. [Sleek Low Bun 2] two loose space buns with falling strands; candid phone-camera warmth
48. [Wavy Middle Part 2] thick dry fluffy waves with natural volume; editorial-clean balance
49. [Messy Space Bun 2] messy layers sweeping across face; natural daylight realism
50. [Soft Layered Lob 2] shaggy bob with choppy texture; soft K-beauty finish
51. [Mirror Glass Straight 3] sharp blunt bob at jawline with clean ends; candid phone-camera warmth
52. [Natural Long Straight 3] low loose bun with natural stray hairs; editorial-clean balance
53. [Blunt Chin Bob 3] straight hair with soft side part; natural daylight realism
54. [Matte Silk Straight 3] two loose space buns with falling strands; soft K-beauty finish
55. [Airy Hush Cut 3] thick dry fluffy waves with natural volume; candid phone-camera warmth
56. [Romantic Dry Waves 3] messy layers sweeping across face; editorial-clean balance
57. [Beach Messy Waves 3] shaggy bob with choppy texture; natural daylight realism
58. [Voluminous Blowout 3] long straight hair with natural weight and subtle sheen; soft K-beauty finish
59. [High Sleek Ponytail 3] high tight ponytail with smooth scalp and dynamic tail; candid phone-camera warmth
60. [Low Effortless Bun 3] translucent baby hairs along the hairline; editorial-clean balance
61. [Half-Up Romantic 3] soft waves with middle part; natural daylight realism
62. [Messy Fluffy Updo 3] heavily layered hush cut with airy face-framing strands; soft K-beauty finish
63. [Wind-Swept Layers 3] loosely pinned updo with protruding strands; candid phone-camera warmth
64. [Natural Damp Glow 3] long hair with curtain bangs; editorial-clean balance
65. [Candid Disheveled 3] sleek black straight hair with center part and high-gloss strands; natural daylight realism
66. [Fine Baby Hair Focus 3] bouncy blow-dried crown volume with soft curves; soft K-beauty finish
67. [Side Part Straight 3] tangled bed hair with realistic friction texture; candid phone-camera warmth
68. [Loose Low Ponytail 3] polished sleek low bun; editorial-clean balance
69. [Soft Curtain Bangs 3] matte smooth straight hair with layered volume; natural daylight realism
70. [Textured Shaggy Bob 3] half-up tie with lower waves flowing; soft K-beauty finish
71. [Half-Up Top Knot 3] loose low ponytail with falling strands; candid phone-camera warmth
72. [Sleek Low Bun 3] collarbone-length layered lob with airy ends; editorial-clean balance
73. [Wavy Middle Part 3] irregular rough sea waves with matte salt texture; natural daylight realism
74. [Messy Space Bun 3] damp post-wash hair with darker roots and clumped ends; soft K-beauty finish
75. [Soft Layered Lob 3] half-up top knot with loose lower hair; candid phone-camera warmth
76. [Mirror Glass Straight 4] matte smooth straight hair with layered volume; editorial-clean balance
77. [Natural Long Straight 4] half-up tie with lower waves flowing; natural daylight realism
78. [Blunt Chin Bob 4] loose low ponytail with falling strands; soft K-beauty finish
79. [Matte Silk Straight 4] collarbone-length layered lob with airy ends; candid phone-camera warmth
80. [Airy Hush Cut 4] irregular rough sea waves with matte salt texture; editorial-clean balance
81. [Romantic Dry Waves 4] damp post-wash hair with darker roots and clumped ends; natural daylight realism
82. [Beach Messy Waves 4] half-up top knot with loose lower hair; soft K-beauty finish
83. [Voluminous Blowout 4] sharp blunt bob at jawline with clean ends; candid phone-camera warmth
84. [High Sleek Ponytail 4] low loose bun with natural stray hairs; editorial-clean balance
85. [Low Effortless Bun 4] straight hair with soft side part; natural daylight realism
86. [Half-Up Romantic 4] two loose space buns with falling strands; soft K-beauty finish
87. [Messy Fluffy Updo 4] thick dry fluffy waves with natural volume; candid phone-camera warmth
88. [Wind-Swept Layers 4] messy layers sweeping across face; editorial-clean balance
89. [Natural Damp Glow 4] shaggy bob with choppy texture; natural daylight realism
90. [Candid Disheveled 4] long straight hair with natural weight and subtle sheen; soft K-beauty finish
91. [Fine Baby Hair Focus 4] high tight ponytail with smooth scalp and dynamic tail; candid phone-camera warmth
92. [Side Part Straight 4] translucent baby hairs along the hairline; editorial-clean balance
93. [Loose Low Ponytail 4] soft waves with middle part; natural daylight realism
94. [Soft Curtain Bangs 4] heavily layered hush cut with airy face-framing strands; soft K-beauty finish
95. [Textured Shaggy Bob 4] loosely pinned updo with protruding strands; candid phone-camera warmth
96. [Half-Up Top Knot 4] long hair with curtain bangs; editorial-clean balance
97. [Sleek Low Bun 4] sleek black straight hair with center part and high-gloss strands; natural daylight realism
98. [Wavy Middle Part 4] bouncy blow-dried crown volume with soft curves; soft K-beauty finish
99. [Messy Space Bun 4] tangled bed hair with realistic friction texture; candid phone-camera warmth
100. [Soft Layered Lob 4] polished sleek low bun; editorial-clean balance

## Section 5: Adult Body Silhouette Bank (100)

1. [Balanced Idol Fit 1] adult balanced proportions with a healthy fashion-model fit; natural daylight realism
2. [Soft Athletic 1] healthy hourglass shape without exaggeration; soft K-beauty finish
3. [Elegant Tall 1] slim-curvy adult silhouette; candid phone-camera warmth
4. [Petite Balanced 1] soft athletic tone with natural curves; editorial-clean balance
5. [Graceful S-Line 1] long-leg ratio and casual confidence; natural daylight realism
6. [Natural Curves 1] modern muse proportions with calm confidence; soft K-beauty finish
7. [Lean Dancer 1] elegant tall frame with relaxed posture; candid phone-camera warmth
8. [Healthy Hourglass 1] compact chic frame with neat waistline; editorial-clean balance
9. [Long-Legged Casual 1] relaxed everyday fit with soft curves; natural daylight realism
10. [Compact Chic 1] petite adult frame with balanced proportions; soft K-beauty finish
11. [Refined Proportion 1] refined proportions and graceful shoulders; candid phone-camera warmth
12. [Soft Core Fit 1] confident upright posture and clean lines; editorial-clean balance
13. [Streetwear Fit 1] graceful S-line silhouette in clothing; natural daylight realism
14. [Studio Dancer 1] soft core definition with relaxed stance; soft K-beauty finish
15. [Everyday Slim Curvy 1] soft feminine line with natural waist; candid phone-camera warmth
16. [Modern Muse 1] natural curves with comfortable posture; editorial-clean balance
17. [Relaxed Fit 1] streetwear-friendly fit and natural hips; natural daylight realism
18. [Confident Posture 1] tall casual frame with long stride; soft K-beauty finish
19. [Soft Feminine Line 1] lean dancer build with toned legs; candid phone-camera warmth
20. [Tall Runway Casual 1] studio dancer body with flexible lines; editorial-clean balance
21. [Balanced Idol Fit 2] soft athletic tone with natural curves; natural daylight realism
22. [Soft Athletic 2] long-leg ratio and casual confidence; soft K-beauty finish
23. [Elegant Tall 2] modern muse proportions with calm confidence; candid phone-camera warmth
24. [Petite Balanced 2] elegant tall frame with relaxed posture; editorial-clean balance
25. [Graceful S-Line 2] compact chic frame with neat waistline; natural daylight realism
26. [Natural Curves 2] relaxed everyday fit with soft curves; soft K-beauty finish
27. [Lean Dancer 2] petite adult frame with balanced proportions; candid phone-camera warmth
28. [Healthy Hourglass 2] refined proportions and graceful shoulders; editorial-clean balance
29. [Long-Legged Casual 2] confident upright posture and clean lines; natural daylight realism
30. [Compact Chic 2] graceful S-line silhouette in clothing; soft K-beauty finish
31. [Refined Proportion 2] soft core definition with relaxed stance; candid phone-camera warmth
32. [Soft Core Fit 2] soft feminine line with natural waist; editorial-clean balance
33. [Streetwear Fit 2] natural curves with comfortable posture; natural daylight realism
34. [Studio Dancer 2] streetwear-friendly fit and natural hips; soft K-beauty finish
35. [Everyday Slim Curvy 2] tall casual frame with long stride; candid phone-camera warmth
36. [Modern Muse 2] lean dancer build with toned legs; editorial-clean balance
37. [Relaxed Fit 2] studio dancer body with flexible lines; natural daylight realism
38. [Confident Posture 2] adult balanced proportions with a healthy fashion-model fit; soft K-beauty finish
39. [Soft Feminine Line 2] healthy hourglass shape without exaggeration; candid phone-camera warmth
40. [Tall Runway Casual 2] slim-curvy adult silhouette; editorial-clean balance
41. [Balanced Idol Fit 3] elegant tall frame with relaxed posture; natural daylight realism
42. [Soft Athletic 3] compact chic frame with neat waistline; soft K-beauty finish
43. [Elegant Tall 3] relaxed everyday fit with soft curves; candid phone-camera warmth
44. [Petite Balanced 3] petite adult frame with balanced proportions; editorial-clean balance
45. [Graceful S-Line 3] refined proportions and graceful shoulders; natural daylight realism
46. [Natural Curves 3] confident upright posture and clean lines; soft K-beauty finish
47. [Lean Dancer 3] graceful S-line silhouette in clothing; candid phone-camera warmth
48. [Healthy Hourglass 3] soft core definition with relaxed stance; editorial-clean balance
49. [Long-Legged Casual 3] soft feminine line with natural waist; natural daylight realism
50. [Compact Chic 3] natural curves with comfortable posture; soft K-beauty finish
51. [Refined Proportion 3] streetwear-friendly fit and natural hips; candid phone-camera warmth
52. [Soft Core Fit 3] tall casual frame with long stride; editorial-clean balance
53. [Streetwear Fit 3] lean dancer build with toned legs; natural daylight realism
54. [Studio Dancer 3] studio dancer body with flexible lines; soft K-beauty finish
55. [Everyday Slim Curvy 3] adult balanced proportions with a healthy fashion-model fit; candid phone-camera warmth
56. [Modern Muse 3] healthy hourglass shape without exaggeration; editorial-clean balance
57. [Relaxed Fit 3] slim-curvy adult silhouette; natural daylight realism
58. [Confident Posture 3] soft athletic tone with natural curves; soft K-beauty finish
59. [Soft Feminine Line 3] long-leg ratio and casual confidence; candid phone-camera warmth
60. [Tall Runway Casual 3] modern muse proportions with calm confidence; editorial-clean balance
61. [Balanced Idol Fit 4] petite adult frame with balanced proportions; natural daylight realism
62. [Soft Athletic 4] refined proportions and graceful shoulders; soft K-beauty finish
63. [Elegant Tall 4] confident upright posture and clean lines; candid phone-camera warmth
64. [Petite Balanced 4] graceful S-line silhouette in clothing; editorial-clean balance
65. [Graceful S-Line 4] soft core definition with relaxed stance; natural daylight realism
66. [Natural Curves 4] soft feminine line with natural waist; soft K-beauty finish
67. [Lean Dancer 4] natural curves with comfortable posture; candid phone-camera warmth
68. [Healthy Hourglass 4] streetwear-friendly fit and natural hips; editorial-clean balance
69. [Long-Legged Casual 4] tall casual frame with long stride; natural daylight realism
70. [Compact Chic 4] lean dancer build with toned legs; soft K-beauty finish
71. [Refined Proportion 4] studio dancer body with flexible lines; candid phone-camera warmth
72. [Soft Core Fit 4] adult balanced proportions with a healthy fashion-model fit; editorial-clean balance
73. [Streetwear Fit 4] healthy hourglass shape without exaggeration; natural daylight realism
74. [Studio Dancer 4] slim-curvy adult silhouette; soft K-beauty finish
75. [Everyday Slim Curvy 4] soft athletic tone with natural curves; candid phone-camera warmth
76. [Modern Muse 4] long-leg ratio and casual confidence; editorial-clean balance
77. [Relaxed Fit 4] modern muse proportions with calm confidence; natural daylight realism
78. [Confident Posture 4] elegant tall frame with relaxed posture; soft K-beauty finish
79. [Soft Feminine Line 4] compact chic frame with neat waistline; candid phone-camera warmth
80. [Tall Runway Casual 4] relaxed everyday fit with soft curves; editorial-clean balance
81. [Balanced Idol Fit 5] graceful S-line silhouette in clothing; natural daylight realism
82. [Soft Athletic 5] soft core definition with relaxed stance; soft K-beauty finish
83. [Elegant Tall 5] soft feminine line with natural waist; candid phone-camera warmth
84. [Petite Balanced 5] natural curves with comfortable posture; editorial-clean balance
85. [Graceful S-Line 5] streetwear-friendly fit and natural hips; natural daylight realism
86. [Natural Curves 5] tall casual frame with long stride; soft K-beauty finish
87. [Lean Dancer 5] lean dancer build with toned legs; candid phone-camera warmth
88. [Healthy Hourglass 5] studio dancer body with flexible lines; editorial-clean balance
89. [Long-Legged Casual 5] adult balanced proportions with a healthy fashion-model fit; natural daylight realism
90. [Compact Chic 5] healthy hourglass shape without exaggeration; soft K-beauty finish
91. [Refined Proportion 5] slim-curvy adult silhouette; candid phone-camera warmth
92. [Soft Core Fit 5] soft athletic tone with natural curves; editorial-clean balance
93. [Streetwear Fit 5] long-leg ratio and casual confidence; natural daylight realism
94. [Studio Dancer 5] modern muse proportions with calm confidence; soft K-beauty finish
95. [Everyday Slim Curvy 5] elegant tall frame with relaxed posture; candid phone-camera warmth
96. [Modern Muse 5] compact chic frame with neat waistline; editorial-clean balance
97. [Relaxed Fit 5] relaxed everyday fit with soft curves; natural daylight realism
98. [Confident Posture 5] petite adult frame with balanced proportions; soft K-beauty finish
99. [Soft Feminine Line 5] refined proportions and graceful shoulders; candid phone-camera warmth
100. [Tall Runway Casual 5] confident upright posture and clean lines; editorial-clean balance

## Section 6: Styling Bank (100)

1. [Style 001] cream floral lace-up cotton romper with cinched waist; natural candid framing
2. [Style 002] teddy-bear ribbed camisole and high-waisted shorts set; clean editorial realism
3. [Style 003] white off-shoulder shirt dress with soft opaque layering; warm daily-life mood
4. [Style 004] black lace-trim satin camisole and shorts set; high-detail photo texture
5. [Style 005] pink bow-print two-piece with ruffled edges; natural candid framing
6. [Style 006] red lace-trim spaghetti strap jersey mini dress; clean editorial realism
7. [Style 007] light blue lace camisole shorts set with modest lining; warm daily-life mood
8. [Style 008] pink satin robe set with soft tie; high-detail photo texture
9. [Style 009] gray twist-front crop top with matching lounge shorts; natural candid framing
10. [Style 010] black square-neck crop top and light gray shorts; clean editorial realism
11. [Style 011] white off-shoulder ribbed crop top with lavender shorts; warm daily-life mood
12. [Style 012] gray strapless button crop top with pleated mini skirt; high-detail photo texture
13. [Style 013] gray-white raglan crop top with hot pants; natural candid framing
14. [Style 014] white floral spaghetti-strap romper; clean editorial realism
15. [Style 015] black-white striped racerback tank and shorts; warm daily-life mood
16. [Style 016] white cartoon animal print mini dress; high-detail photo texture
17. [Style 017] white floral bow print lace-trim mini dress; natural candid framing
18. [Style 018] black butterfly print slip dress with lace trim; clean editorial realism
19. [Style 019] blue denim chain-strap mini dress; warm daily-life mood
20. [Style 020] light green denim pinafore mini dress; high-detail photo texture
21. [Style 021] cream crochet halter and denim shorts; natural candid framing
22. [Style 022] white ribbed crop top with denim cutoffs; clean editorial realism
23. [Style 023] brown ribbed turtleneck crop top with denim shorts; warm daily-life mood
24. [Style 024] white off-shoulder ribbed top with dark gray training shorts; high-detail photo texture
25. [Style 025] gray square-neck ribbed crop top with denim hot pants; natural candid framing
26. [Style 026] white ruched crop shirt with leopard pleated mini skirt; clean editorial realism
27. [Style 027] white knit crop top and matching mini skirt with stripe trim; warm daily-life mood
28. [Style 028] black sequined halter crop top with ruffled mini skirt; high-detail photo texture
29. [Style 029] white long-sleeve square-neck crop top with blue ruched mini skirt; natural candid framing
30. [Style 030] red gingham spaghetti-strap mini dress; clean editorial realism
31. [Style 031] striped spaghetti-strap mini dress with black lace trim; warm daily-life mood
32. [Style 032] gray-black striped square-neck ribbed mini dress; high-detail photo texture
33. [Style 033] white scoop-neck crop top with black shorts; natural candid framing
34. [Style 034] black button-up ribbed crop top with dark denim mini skirt; clean editorial realism
35. [Style 035] blue floral off-shoulder ruffled mini dress; warm daily-life mood
36. [Style 036] strawberry print triangle bikini with tie-side bottoms; high-detail photo texture
37. [Style 037] black halter bikini with patterned bottoms; natural candid framing
38. [Style 038] white minimal triangle bikini with beach cover-up nearby; clean editorial realism
39. [Style 039] navy triangle halter bikini; warm daily-life mood
40. [Style 040] blue cherry-print triangle bikini; high-detail photo texture
41. [Style 041] navy one-piece swimsuit; natural candid framing
42. [Style 042] dark taupe bandeau halter bikini; clean editorial realism
43. [Style 043] red heart print bikini; warm daily-life mood
44. [Style 044] white cherry halter bikini set with red trim; high-detail photo texture
45. [Style 045] pink leopard halter bikini; natural candid framing
46. [Style 046] blue-white striped halter bikini; clean editorial realism
47. [Style 047] red gingham halter bikini; warm daily-life mood
48. [Style 048] beige sparkle knit maxi dress with side slit; high-detail photo texture
49. [Style 049] black-white striped halter bodycon mini dress; natural candid framing
50. [Style 050] iridescent rainbow mesh knit set with lining; clean editorial realism
51. [Style 051] warm geometric knit mini dress; warm daily-life mood
52. [Style 052] black peplum tulle mini dress; high-detail photo texture
53. [Style 053] white satin mini qipao; natural candid framing
54. [Style 054] magenta spaghetti-strap bodycon midi dress; clean editorial realism
55. [Style 055] dark teal off-shoulder cutout mesh mini dress; warm daily-life mood
56. [Style 056] bright blue spaghetti-strap mini dress; high-detail photo texture
57. [Style 057] white crochet halter mini dress; natural candid framing
58. [Style 058] white sailor crop top with blue pleated mini skirt; clean editorial realism
59. [Style 059] navy stage-police-inspired costume with lace stockings; warm daily-life mood
60. [Style 060] retro nurse-inspired fashion outfit with red trim; high-detail photo texture
61. [Style 061] chic police-inspired shirt with leather mini skirt; natural candid framing
62. [Style 062] velvet santa-inspired strapless top with mini skirt; clean editorial realism
63. [Style 063] white button-up shirt with navy tie and black mini skirt; warm daily-life mood
64. [Style 064] black sailor uniform dress with white bow; high-detail photo texture
65. [Style 065] oversized pastel hoodie with bike shorts; natural candid framing
66. [Style 066] ivory cable-knit cardigan and pleated skirt; clean editorial realism
67. [Style 067] mint ribbed tank with white tennis skirt; warm daily-life mood
68. [Style 068] cropped denim jacket over floral mini dress; high-detail photo texture
69. [Style 069] linen button shirt tied at waist with shorts; natural candid framing
70. [Style 070] lavender knit bolero with matching cami dress; clean editorial realism
71. [Style 071] pink varsity jacket with white mini skirt; warm daily-life mood
72. [Style 072] black cropped blazer and high-waist shorts; high-detail photo texture
73. [Style 073] cream tube top with loose cargo pants; natural candid framing
74. [Style 074] baby-blue hoodie dress with sneakers; clean editorial realism
75. [Style 075] soft yellow cardigan with denim mini skirt; warm daily-life mood
76. [Style 076] sage wrap top with white shorts; high-detail photo texture
77. [Style 077] striped knit polo mini dress; natural candid framing
78. [Style 078] charcoal cropped sweatshirt with pleated skirt; clean editorial realism
79. [Style 079] white eyelet summer dress; warm daily-life mood
80. [Style 080] black mock-neck sleeveless mini dress; high-detail photo texture
81. [Style 081] red knit cardigan with denim shorts; natural candid framing
82. [Style 082] ivory satin slip dress with cardigan; clean editorial realism
83. [Style 083] powder-blue puff-sleeve mini dress; warm daily-life mood
84. [Style 084] khaki utility mini dress; high-detail photo texture
85. [Style 085] rose floral wrap mini dress; natural candid framing
86. [Style 086] black mesh-sleeve party mini dress with lining; clean editorial realism
87. [Style 087] cream tweed crop jacket with mini skirt; warm daily-life mood
88. [Style 088] silver lamé stage mini dress; high-detail photo texture
89. [Style 089] pastel tracksuit crop jacket with shorts; natural candid framing
90. [Style 090] white tennis club dress; clean editorial realism
91. [Style 091] green halter knit top with beige shorts; warm daily-life mood
92. [Style 092] navy cropped rugby shirt with white skirt; high-detail photo texture
93. [Style 093] soft pink lounge jumpsuit; natural candid framing
94. [Style 094] terracotta linen romper; clean editorial realism
95. [Style 095] gray ballet wrap cardigan with black skirt; warm daily-life mood
96. [Style 096] ivory bandeau top with high-waist wide pants; high-detail photo texture
97. [Style 097] brown suede mini dress; natural candid framing
98. [Style 098] black satin bow top with pleated skirt; clean editorial realism
99. [Style 099] aqua resort maxi dress; warm daily-life mood
100. [Style 100] white cropped tee with plaid mini skirt; high-detail photo texture

## Section 7: Iconic Pose Bank (100)

1. [Pose 001] casual lean against a wall; natural candid framing
2. [Pose 002] over-the-shoulder look with hair touch; clean editorial realism
3. [Pose 003] morning stretch with arms raised; warm daily-life mood
4. [Pose 004] sinking into a sofa; high-detail photo texture
5. [Pose 005] standing by a window with hand on glass; natural candid framing
6. [Pose 006] bed recline propped on elbows; clean editorial realism
7. [Pose 007] gentle head tilt with eye contact; warm daily-life mood
8. [Pose 008] running fingers through hair; high-detail photo texture
9. [Pose 009] knee hug while seated; natural candid framing
10. [Pose 010] side sit on edge of sofa; clean editorial realism
11. [Pose 011] mirror reflection while fixing hair; warm daily-life mood
12. [Pose 012] reaching toward window light; high-detail photo texture
13. [Pose 013] floor sit with one leg bent; natural candid framing
14. [Pose 014] gentle back arch while standing; clean editorial realism
15. [Pose 015] playful glance over shoulder; warm daily-life mood
16. [Pose 016] relaxed yawn with arms behind head; high-detail photo texture
17. [Pose 017] natural crossed-leg sit; natural candid framing
18. [Pose 018] wall lean with one knee bent; clean editorial realism
19. [Pose 019] arm draped over sofa; warm daily-life mood
20. [Pose 020] gentle crouch looking up; high-detail photo texture
21. [Pose 021] side recline with relaxed posture; natural candid framing
22. [Pose 022] hand on hip with S-line stance; clean editorial realism
23. [Pose 023] tying hair with arms raised; warm daily-life mood
24. [Pose 024] quiet contemplation with unfocused gaze; high-detail photo texture
25. [Pose 025] mid-stride walk toward camera; natural candid framing
26. [Pose 026] floor pose with legs extended; clean editorial realism
27. [Pose 027] standing with weight on one hip; warm daily-life mood
28. [Pose 028] gentle shoulder shrug; high-detail photo texture
29. [Pose 029] soft hand on neck; natural candid framing
30. [Pose 030] relaxed crossed arms; clean editorial realism
31. [Pose 031] checking phone while leaning; warm daily-life mood
32. [Pose 032] holding coffee cup near chest; high-detail photo texture
33. [Pose 033] adjusting earring; natural candid framing
34. [Pose 034] smoothing skirt hem; clean editorial realism
35. [Pose 035] pulling cardigan sleeve; warm daily-life mood
36. [Pose 036] turning around mid-step; high-detail photo texture
37. [Pose 037] looking down at shoes; natural candid framing
38. [Pose 038] resting chin on hand; clean editorial realism
39. [Pose 039] reading a book with soft gaze; warm daily-life mood
40. [Pose 040] opening balcony door; high-detail photo texture
41. [Pose 041] lifting sunglasses; natural candid framing
42. [Pose 042] fixing ribbon tie; clean editorial realism
43. [Pose 043] holding tote bag strap; warm daily-life mood
44. [Pose 044] reaching for makeup brush; high-detail photo texture
45. [Pose 045] sitting sideways on chair; natural candid framing
46. [Pose 046] kneeling on rug casually; clean editorial realism
47. [Pose 047] leaning over kitchen island; warm daily-life mood
48. [Pose 048] peeking from doorway; high-detail photo texture
49. [Pose 049] hugging cushion; natural candid framing
50. [Pose 050] standing on tiptoe; clean editorial realism
51. [Pose 051] brushing hair behind ear; warm daily-life mood
52. [Pose 052] soft wave to camera; high-detail photo texture
53. [Pose 053] checking mirror outfit; natural candid framing
54. [Pose 054] holding flower bouquet; clean editorial realism
55. [Pose 055] sipping iced drink; warm daily-life mood
56. [Pose 056] stretching leg after walk; high-detail photo texture
57. [Pose 057] looking at city view; natural candid framing
58. [Pose 058] resting on pool lounger; clean editorial realism
59. [Pose 059] folding laundry casually; warm daily-life mood
60. [Pose 060] opening closet door; high-detail photo texture
61. [Pose 061] writing in notebook; natural candid framing
62. [Pose 062] placing headphones on; clean editorial realism
63. [Pose 063] walking stairs upward; warm daily-life mood
64. [Pose 064] leaning on balcony rail; high-detail photo texture
65. [Pose 065] turning page of magazine; natural candid framing
66. [Pose 066] sitting on window sill; clean editorial realism
67. [Pose 067] lifting camera strap; warm daily-life mood
68. [Pose 068] holding umbrella handle; high-detail photo texture
69. [Pose 069] adjusting ponytail; natural candid framing
70. [Pose 070] soft clap during laugh; clean editorial realism
71. [Pose 071] taking one step back; warm daily-life mood
72. [Pose 072] looking through curtains; high-detail photo texture
73. [Pose 073] holding cereal bowl; natural candid framing
74. [Pose 074] tying sneaker laces; clean editorial realism
75. [Pose 075] standing with hands in pockets; warm daily-life mood
76. [Pose 076] half-turn profile pose; high-detail photo texture
77. [Pose 077] leaning on cafe table; natural candid framing
78. [Pose 078] curling legs on armchair; clean editorial realism
79. [Pose 079] touching necklace pendant; warm daily-life mood
80. [Pose 080] holding perfume bottle; high-detail photo texture
81. [Pose 081] zipping small handbag; natural candid framing
82. [Pose 082] watching rain outside; clean editorial realism
83. [Pose 083] posing with skateboard nearby; warm daily-life mood
84. [Pose 084] resting elbows on counter; high-detail photo texture
85. [Pose 085] turning head toward sound; natural candid framing
86. [Pose 086] lifting hair in breeze; clean editorial realism
87. [Pose 087] holding a folded jacket; warm daily-life mood
88. [Pose 088] soft salute pose; high-detail photo texture
89. [Pose 089] crossing ankles while seated; natural candid framing
90. [Pose 090] looking into compact mirror; clean editorial realism
91. [Pose 091] leaning out car window safely; warm daily-life mood
92. [Pose 092] holding beach towel; high-detail photo texture
93. [Pose 093] placing hat on head; natural candid framing
94. [Pose 094] stepping through doorway; clean editorial realism
95. [Pose 095] balancing on curb; warm daily-life mood
96. [Pose 096] reaching for book shelf; high-detail photo texture
97. [Pose 097] holding shopping bag; natural candid framing
98. [Pose 098] resting hand on railing; clean editorial realism
99. [Pose 099] soft laugh with shoulders forward; warm daily-life mood
100. [Pose 100] slow dance step in room; high-detail photo texture

## Section 8: Daily Life Scene Bank (100)

1. [Scene 001] morning bedroom with messy bed and window glow; natural candid framing
2. [Scene 002] cozy living room sofa with lamp and daylight; clean editorial realism
3. [Scene 003] balcony golden hour with city greenery; warm daily-life mood
4. [Scene 004] urban sidewalk casual walk; high-detail photo texture
5. [Scene 005] cafe window seat with wooden table; natural candid framing
6. [Scene 006] bright kitchen counter; clean editorial realism
7. [Scene 007] dressing room mirror with soft studio light; warm daily-life mood
8. [Scene 008] hotel balcony with ocean or city view; high-detail photo texture
9. [Scene 009] car interior with window daylight; natural candid framing
10. [Scene 010] rooftop sunset with backlit skyline; clean editorial realism
11. [Scene 011] walk-in closet with warm lights; warm daily-life mood
12. [Scene 012] bathroom vanity with natural light; high-detail photo texture
13. [Scene 013] outdoor cafe terrace; natural candid framing
14. [Scene 014] bedroom floor with cozy window light; clean editorial realism
15. [Scene 015] gym mirror with bright studio light; warm daily-life mood
16. [Scene 016] library corner with bookshelves; high-detail photo texture
17. [Scene 017] poolside lounge in bright sunlight; natural candid framing
18. [Scene 018] night bedroom with warm lamp; clean editorial realism
19. [Scene 019] street fashion walk in daylight; warm daily-life mood
20. [Scene 020] vanity table with ring light; high-detail photo texture
21. [Scene 021] balcony morning coffee; natural candid framing
22. [Scene 022] living room rug with natural light; clean editorial realism
23. [Scene 023] hotel room window; warm daily-life mood
24. [Scene 024] outdoor park bench; high-detail photo texture
25. [Scene 025] modern apartment kitchen island; natural candid framing
26. [Scene 026] sunlit terrace; clean editorial realism
27. [Scene 027] cozy reading nook; warm daily-life mood
28. [Scene 028] bathroom mirror selfie angle; high-detail photo texture
29. [Scene 029] rooftop city view; natural candid framing
30. [Scene 030] bedroom window seat; clean editorial realism
31. [Scene 031] laundry room with soft afternoon light; warm daily-life mood
32. [Scene 032] flower shop doorway; high-detail photo texture
33. [Scene 033] convenience store night exterior; natural candid framing
34. [Scene 034] subway platform daytime; clean editorial realism
35. [Scene 035] museum hallway; warm daily-life mood
36. [Scene 036] record store aisle; high-detail photo texture
37. [Scene 037] dance practice studio; natural candid framing
38. [Scene 038] backstage dressing area; clean editorial realism
39. [Scene 039] makeup studio chair; warm daily-life mood
40. [Scene 040] small bookstore window; high-detail photo texture
41. [Scene 041] greenhouse cafe; natural candid framing
42. [Scene 042] rainy street under awning; clean editorial realism
43. [Scene 043] beach boardwalk; warm daily-life mood
44. [Scene 044] resort pool cabana; high-detail photo texture
45. [Scene 045] quiet hotel corridor; natural candid framing
46. [Scene 046] apartment elevator mirror; clean editorial realism
47. [Scene 047] stairwell with skylight; warm daily-life mood
48. [Scene 048] university campus path; high-detail photo texture
49. [Scene 049] picnic blanket in park; natural candid framing
50. [Scene 050] riverside walking path; clean editorial realism
51. [Scene 051] city crosswalk; warm daily-life mood
52. [Scene 052] boutique fitting room; high-detail photo texture
53. [Scene 053] photo booth lobby; natural candid framing
54. [Scene 054] arcade corner; clean editorial realism
55. [Scene 055] karaoke room hallway; warm daily-life mood
56. [Scene 056] night market stall; high-detail photo texture
57. [Scene 057] bakery counter; natural candid framing
58. [Scene 058] tea house tatami corner; clean editorial realism
59. [Scene 059] minimal white studio; warm daily-life mood
60. [Scene 060] industrial loft window; high-detail photo texture
61. [Scene 061] pastel bedroom vanity; natural candid framing
62. [Scene 062] sunny breakfast table; clean editorial realism
63. [Scene 063] rooftop garden; warm daily-life mood
64. [Scene 064] train window seat; high-detail photo texture
65. [Scene 065] airport lounge; natural candid framing
66. [Scene 066] boutique hotel lobby; clean editorial realism
67. [Scene 067] garden patio; warm daily-life mood
68. [Scene 068] winter street with soft scarf mood; high-detail photo texture
69. [Scene 069] spring cherry blossom path; natural candid framing
70. [Scene 070] summer beach umbrella; clean editorial realism
71. [Scene 071] autumn park path; warm daily-life mood
72. [Scene 072] snowy cafe window; high-detail photo texture
73. [Scene 073] neon alley fashion shot; natural candid framing
74. [Scene 074] quiet bridge at dusk; clean editorial realism
75. [Scene 075] apartment balcony laundry line; warm daily-life mood
76. [Scene 076] home office desk; high-detail photo texture
77. [Scene 077] music room with keyboard; natural candid framing
78. [Scene 078] pet-friendly cafe; clean editorial realism
79. [Scene 079] art studio easel; warm daily-life mood
80. [Scene 080] ceramic workshop table; high-detail photo texture
81. [Scene 081] yoga mat corner; natural candid framing
82. [Scene 082] pilates studio window; clean editorial realism
83. [Scene 083] tennis court fence; warm daily-life mood
84. [Scene 084] basketball court sideline; high-detail photo texture
85. [Scene 085] skate park edge; natural candid framing
86. [Scene 086] flower field path; clean editorial realism
87. [Scene 087] mountain resort deck; warm daily-life mood
88. [Scene 088] lakeside pier; high-detail photo texture
89. [Scene 089] camping glamping tent; natural candid framing
90. [Scene 090] farmers market aisle; clean editorial realism
91. [Scene 091] supermarket fruit section; warm daily-life mood
92. [Scene 092] department store escalator; high-detail photo texture
93. [Scene 093] hotel bathroom marble vanity; natural candid framing
94. [Scene 094] walkway by glass buildings; clean editorial realism
95. [Scene 095] old town stone alley; warm daily-life mood
96. [Scene 096] seaside cafe terrace; high-detail photo texture
97. [Scene 097] indoor pool window; natural candid framing
98. [Scene 098] penthouse living room; clean editorial realism
99. [Scene 099] private cinema lounge; warm daily-life mood
100. [Scene 100] quiet chapel garden; high-detail photo texture

## Output Template

When triggered, output four separate prompts like this:

### Image Prompt 1

`[assembled single-image prompt]`

### Image Prompt 2

`[assembled single-image prompt]`

### Image Prompt 3

`[assembled single-image prompt]`

### Image Prompt 4

`[assembled single-image prompt]`

Then run four separate image-generation jobs if the environment supports multiple image calls. If only one image call is available per response, run Image Prompt 1 first and continue automatically with Image Prompt 2, 3, and 4 in separate calls.
