import requests
import os


VOICE_ID = "pNInz6obpgDQGcFmaJgB"


def generate_voice(text):
    api_key = os.getenv("ELEVENLABS_API_KEY")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.35,
            "similarity_boost": 0.8,
            "style": 0.7,
            "use_speaker_boost": True
        }
    }

    response = requests.post(url, json=data, headers=headers)

    with open("temp/voice.mp3", "wb") as f:
        f.write(response.content)
