import gradio as gr
import requests
import os
import re

# 👂 Word replacements for better pronunciation
REPLACEMENTS = {
    "Abuja": "Ah-boo-jah",
    "dey": "day",
    "wahala": "wa-ha-la",
    "wetin": "weh-teen",
    "no wahala": "no wa-ha-la",
    "abi": "ah-bee",
    "how far": "hao fa",
    "go come": "go kohm",
    "waka": "wah-kah"
}

def apply_custom_replacements(text):
    # Case-insensitive replacements
    for original, phonetic in REPLACEMENTS.items():
        text = re.sub(rf"\b{original}\b", phonetic, text, flags=re.IGNORECASE)
    return text

# Define available voice options and their corresponding IDs
VOICE_OPTIONS = {
    "Pidgin Voice Female": "eOHsvebhdtt0XFeHVMQY",
    "Pidgin Voice Male": "LEvd0YiWkwZ6hTZOmdVE",  # Example ID, replace with actual
    # Add more voices here if available, e.g. "Voice 2": "another_voice_id"
}

def generate_pidgin_audio(text, voice_label):
    voice_id = VOICE_OPTIONS[voice_label]
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": "sk_8c2a27c36661b27c1768cb48985e04601933e23f1a741123",  # Replace with your actual API key
        "Content-Type": "application/json"
    }

    # 🧠 Fix common Pidgin mispronunciations
    fixed_text = apply_custom_replacements(text)

    # 🐌 Optional: slow pacing using punctuation
    slow_text = fixed_text.replace(",", ", ").replace(".", ". ").replace("?", "? ").replace("!", "! ")

    payload = {
        "text": slow_text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.3,             # Lower = more variation, better for expressive Pidgin
            "similarity_boost": 0.6    # Lower = slower, more distinct pronunciation
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        audio_path = "Audio_pidgin.mp3"
        with open(audio_path, "wb") as f:
            f.write(response.content)
        return audio_path, audio_path
    else:
        print("Error:", response.status_code, response.text)
        return None, None
    
# 🎨 Gradio App UI
with gr.Blocks() as app:
    gr.Markdown("## 🗣️ Naija Pidgin Text-to-Speech App")
    gr.Markdown("Convert your Pidgin English 🔤 to sweet voice 🎧 using AI!")

    with gr.Row():
        text_input = gr.Textbox(label="✍️ Enter Pidgin Text", placeholder="Wetin dey happen today for Abuja?")
        voice_dropdown = gr.Dropdown(choices=list(VOICE_OPTIONS.keys()), label="🎙️ Choose a Voice")

    generate_btn = gr.Button("🔊 Generate Audio")

    audio_output = gr.Audio(label="🎧 Audio Player")
    download_output = gr.File(label="⬇️ Download Audio")

    generate_btn.click(
        fn=generate_pidgin_audio,
        inputs=[text_input, voice_dropdown],
        outputs=[audio_output, download_output]
    )

app.launch(share=True)
