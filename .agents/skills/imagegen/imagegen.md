---
name: imagegen
description: Generate or edit images from prompts using the OpenAI image generation API. Use when the user asks to create, draw, render, generate, or edit image assets, thumbnails, sprites, mockups, concept art, backgrounds, or visual references.
Image Generation Skill
Use this skill when the user asks for image generation or image editing.
Core behavior
Convert the user's request into a clean, production-ready image prompt.
Preserve the user's requested subject, pose, composition, clothing, lighting, camera angle, style, and aspect ratio.
Ask only when a critical detail is missing.
Save generated image files into ./generated/.
For multiple images, generate separate image files, not a collage, unless the user explicitly asks for a grid.
Do not overwrite existing files unless the user asks.
After generation, report the output file paths.
Quality policy
Always prioritize maximum visual quality.
Use:
quality: high
highly detailed prompt wording
clean composition instructions
explicit aspect ratio / size selection
separate files for variations
PNG output unless the user asks otherwise
Avoid:
low-resolution outputs
blurry results
compressed JPEG unless requested
accidental collage output
unwanted text, watermark, logo, signature, UI overlay, or extra captions
distorted hands, duplicated limbs, broken anatomy, plastic texture, over-smoothed AI skin
Default size and aspect-ratio rules
Choose the output size based on the user's requested format.
Vertical portrait / full-body / character image
Use this by default for people, fashion, character sheets, full-body shots, vertical posters, and mobile wallpaper.
Command size: --size 1024x1536
Aspect ratio: 2:3 vertical
Square image
Use for album covers, icons, profile images, product mockups, stickers, and centered concept art.
Command size: --size 1024x1024
Aspect ratio: 1:1 square
Landscape image
Use for cinematic stills, web headers, wide scenes, horizontal compositions, and general landscape images.
Command size: --size 1536x1024
Aspect ratio: 3:2 landscape
Wide thumbnail / banner
Use when the user asks for 16:9, YouTube thumbnail, cinematic frame, broadcast frame, or wide banner.
Preferred command size: --size 1536x864
Aspect ratio: 16:9 landscape
Fallback: if the API does not support this exact size, use the closest supported landscape size and preserve the 16:9 composition in the prompt.
Tall mobile / story format
Use when the user asks for 9:16, Instagram story, TikTok style, phone wallpaper, or vertical full-screen image.
Preferred command size: --size 864x1536
Aspect ratio: 9:16 vertical
Fallback: if the API does not support this exact size, use the closest supported vertical size and preserve the 9:16 composition in the prompt.
Prompt rules
When creating prompts, include:
subject
action
environment
camera angle
lens or camera style if requested
lighting
composition
material and texture details
mood
aspect ratio
quality instructions
negative constraints
Default negative constraints:
no watermark, no logo, no random text, no extra captions, no distorted hands, no duplicated limbs, no broken anatomy, no low-resolution artifacts, no over-smoothed AI skin, no plastic texture
Script usage
Use this command pattern for image generation:
python .agents/skills/imagegen/scripts/generate_image.py --prompt "A cinematic photorealistic scene..." --output generated/image_001.png --size 1024x1536 --quality high
For four separate images, run the same script four times with separate output filenames:
python .agents/skills/imagegen/scripts/generate_image.py --prompt "Variation 1 prompt..." --output generated/image_001.png --size 1024x1536 --quality high
python .agents/skills/imagegen/scripts/generate_image.py --prompt "Variation 2 prompt..." --output generated/image_002.png --size 1024x1536 --quality high
python .agents/skills/imagegen/scripts/generate_image.py --prompt "Variation 3 prompt..." --output generated/image_003.png --size 1024x1536 --quality high
python .agents/skills/imagegen/scripts/generate_image.py --prompt "Variation 4 prompt..." --output generated/image_004.png --size 1024x1536 --quality high
Batch generation rule
If the user says any of the following:
4장 뽑아줘
총 4개
4 variations
generate 4 images
Then generate four separate files:
generated/image_001.png
generated/image_002.png
generated/image_003.png
generated/image_004.png
Do not make one 2x2 collage unless the user explicitly says one of the following:
2x2 grid
collage
one image containing four panels
