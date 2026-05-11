import whisper
import os
import logging

def format_time(seconds):
    """تحويل الثواني إلى تنسيق SRT القياسي (00:00:00,000)"""
    milliseconds = int((seconds - int(seconds)) * 1000)
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds_int = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds_int:02},{milliseconds:03}"

def generate_captions(audio_path):
    try:
        # 1. تحميل النموذج (يفضل استخدام 'small' للعربية لدقة أفضل من 'base')
        model = whisper.load_model("small") 

        # 2. تنفيذ النسخ مع تحديد اللغة لزيادة السرعة والدقة
        logging.info("Transcribing audio for captions...")
        result = model.transcribe(audio_path, language='ar', task='transcribe')

        segments = result["segments"]
        os.makedirs("temp", exist_ok=True)
        srt_path = "temp/captions.srt"

        with open(srt_path, "w", encoding="utf-8") as f:
            for i, segment in enumerate(segments):
                start = segment["start"]
                end = segment["end"]
                text = segment["text"].strip()

                # تنسيق الوقت بشكل احترافي متوافق مع كافة برامج الرندرة
                start_srt = format_time(start)
                end_srt = format_time(end)

                f.write(f"{i+1}\n")
                f.write(f"{start_srt} --> {end_srt}\n")
                f.write(f"{text}\n\n")

        logging.info(f"✅ Captions saved to: {srt_path}")
        return srt_path

    except Exception as e:
        logging.error(f"❌ Whisper error: {str(e)}")
        return None
