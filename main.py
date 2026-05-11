import logging
import os
from engine.ai.script_generator import generate_script
from engine.audio.voice_generator import generate_voice
from engine.video.pixabay_fetcher import fetch_video
from engine.captions.captions import generate_captions
from engine.render.renderer import render_video

# إعداد السجلات (Logging) بدلاً من البرينت العادي
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def run_pipeline():
    try:
        # 1. إنشاء السيناريو
        logging.info("Generating cinematic script...")
        script = generate_script()
        if not script:
            raise ValueError("Script generation failed!")

        # 2. إنشاء الصوت (إرجاع المسار بدلاً من الاعتماد على مسار ثابت)
        logging.info("Generating AI voice...")
        voice_path = generate_voice(script) 
        
        # 3. تحميل المشاهد (تأكد من تحميل مشاهد كافية لطول الفيديو)
        logging.info("Downloading cinematic footage...")
        video_clips = fetch_video()

        # 4. توليد الترجمة بناءً على ملف الصوت المنشأ
        logging.info("Generating captions...")
        captions = generate_captions(voice_path)

        # 5. الرندرة النهائية
        logging.info("Rendering final cinematic video...")
        output_path = render_video(video_clips, voice_path, captions)

        logging.info(f"✅ Done! Video saved at: {output_path}")

    except Exception as e:
        logging.error(f"❌ Pipeline failed: {str(e)}")

if __name__ == "__main__":
    run_pipeline()
