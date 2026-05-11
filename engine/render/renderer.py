import os
import logging
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip

def render_video():
    try:
        # 1. تحميل الملفات الأساسية
        audio = AudioFileClip("temp/voice.mp3")
        video = VideoFileClip("temp/clip.mp4")

        # 2. ضبط الأبعاد (Crop to 9:16)
        # بدلاً من resize العادي الذي قد يسبب "تمطيط" للصورة، نستخدم المحاذاة المركزية
        w, h = video.size
        target_ratio = 1080 / 1920
        current_ratio = w / h

        if current_ratio > target_ratio:
            # الفيديو عريض جداً -> قص الجوانب
            new_w = h * target_ratio
            video = video.crop(x_center=w/2, width=new_w)
        else:
            # الفيديو طويل جداً -> قص الأعلى والأسفل
            new_h = w / target_ratio
            video = video.crop(y_center=h/2, height=new_h)

        video = video.resize((1080, 1920)).subclip(0, audio.duration)

        # 3. دمج الترجمة (Captions)
        def generator(txt):
            return TextClip(
                txt,
                font="assets/fonts/Anton-Regular.ttf",
                fontsize=80,
                color='white',
                stroke_color='black',
                stroke_width=2,
                method='caption',
                size=(video.w * 0.8, None)
            ).set_position(('center', 'center'))

        if os.path.exists("temp/captions.srt"):
            subtitles = SubtitlesClip("temp/captions.srt", generator)
            video = CompositeVideoClip([video, subtitles.set_position(('center', 'center'))])

        # 4. دمج الصوت النهائي
        final_video = video.set_audio(audio)

        # 5. تصدير الفيديو بأفضل إعدادات للمنصات
        output_path = "output/final.mp4"
        os.makedirs("output", exist_ok=True)
        
        final_video.write_videofile(
            output_path,
            fps=30, # 30fps كافية جداً لنمط الـ Luxury وتسرع الرندرة
            codec="libx264",
            audio_codec="aac",
            temp_audiofile='temp/temp-audio.m4a',
            remove_temp=True,
            preset="medium", # توازن بين السرعة وحجم الملف
            threads=os.cpu_count() # استخدام كامل قوة المعالج
        )

        # تنظيف الذاكرة
        video.close()
        audio.close()
        
        return output_path

    except Exception as e:
        logging.error(f"❌ Rendering failed: {str(e)}")
        return None
