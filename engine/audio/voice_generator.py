import requests
import os
import logging

# صوت Adam الشهير للمحتوى التحفيزي
VOICE_ID = "pNInz6obpgDQGcFmaJgB"

def generate_voice(text):
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        logging.error("ElevenLabs API Key is missing!")
        return None

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    # إعدادات محسنة لنبرة "الفخامة والغموض"
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.45,       # رفع الاستقرار قليلاً لمنع تقطع الصوت في العربية
            "similarity_boost": 0.85, 
            "style": 0.55,           # تقليل الستايل لزيادة الجدية والرزانة
            "use_speaker_boost": True
        }
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        
        # التحقق من نجاح الطلب قبل الحفظ
        if response.status_code == 200:
            os.makedirs("temp", exist_ok=True)
            file_path = "temp/voice.mp3"
            with open(file_path, "wb") as f:
                f.write(response.content)
            logging.info("✅ Audio generated successfully.")
            return file_path
        else:
            logging.error(f"❌ ElevenLabs Error: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        logging.error(f"❌ Connection error: {str(e)}")
        return None
