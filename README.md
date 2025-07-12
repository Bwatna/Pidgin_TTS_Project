# Pidgin_TTS_Project
Pidgin Text-To-Speech using ElevenLab.ai, Gradio and VSCode 
## Language Focus
The project focuses on **Nigerian Pidgin English**, a widely spoken and informal language in Nigeria. It's used in daily conversations, music, and street gists.
## Voices Used
voices_ID Male:"LEvd0YiWkwZ6hTZOmdVE"
Voices_ID Female:"eOHsvebhdtt0XFeHVMQY"
## Handling Pronunciation
- We used ElevenLabs' `eleven_multilingual_v2` model for improved pronunciation of African dialects.
- Adjusted `stability` and `similarity_boost` to slow down speech and enhance clarity.
- Introduced a replacement dictionary in future versions to fix common mispronunciations.
- Text inputs can be structured with informal spelling to guide pronunciation (e.g. *"dey"*, *"waka"*, *"abi"*).
 Also slowed down speech slightly using:
- Lower stability (`0.3`)
- Slight punctuation spacing
- Word breaks using commas and spaces

## Features
-  Text input for Pidgin
-  Voice dropdown
-  Generate audio with ElevenLabs
-  Audio playback
-  Download audio file
-  Clean UI with emojis
# Tech Stack
- Python 
- Gradio for UI 
- ElevenLabs API for TTS 
