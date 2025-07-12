import gradio as gr
import requests
import os

# 🔐 Replace with your actual ElevenLabs API key
API_KEY = "sk_f6c952445695d0c28fa1ac2e4938a696bd4a2d4c77d4b1c5"

# 🗣️ Voice dictionary: Replace "voice_id_here" with your actual voice ID
VOICE_OPTIONS = {
    "Pidgin Voice 🔊": "Z8dg0fyk7p6js7cQ7lgi"  # Example ID you mentioned
}

# 🎯 Text-to-Speech function using ElevenLabs
def generate_pidgin_audio(text, voice_label):
    voice_id = VOICE_OPTIONS[voice_label]
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    # 🧠 Optional: Slow down reading using punctuation
    slow_text = text.replace(",", ", ").replace(".", ". ").replace("?", "? ").replace("!", "! ")

    payload = {
        "text": slow_text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 1,             # Lower = more variation, better for expressive Pidgin
            "similarity_boost": 0.75      # Lower = slower, more distinct pronunciation
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        audio_path = "pidgin_Audio4.mp3"
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




