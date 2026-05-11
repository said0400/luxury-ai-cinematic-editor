from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
import os

def render_video(downloaded_paths, voice_path, captions_path):
    try:
        # 1. تحميل الصوت لمعرفة المدة الإجمالية المطلوبة
        audio = AudioFileClip(voice_path)
        
        # 2. معالجة قائمة المقاطع وتحويلها إلى كليبات MoviePy
        # هنا نضيف الكود الذي سألت عنه مع تحسين بسيط لضبط الأبعاد
        clips = []
        for p in downloaded_paths:
            clip = VideoFileClip(p).resize(height=1920) # ضبط الطول ليتناسب مع التيك توك
            # قص العرض ليكون 1080 (Crop to Center)
            w, h = clip.size
            clip = clip.crop(x_center=w/2, width=1080)
            clips.append(clip)

        # 3. دمج المقاطع في خلفية واحدة متصلة
        # نستخدم method="compose" لضمان عدم حدوث مشاكل في حال اختلاف جودة المقاطع
        final_video_bg = concatenate_videoclips(clips, method="compose")

        # 4. قص الخلفية لتناسب مدة الصوت تماماً
        final_video_bg = final_video_bg.subclip(0, audio.duration)

        # 5. إضافة الترجمة (Captions) فوق الخلفية المدمجة
        # (نفترض وجود دالة generator للخط كما في الرد السابق)
        if os.path.exists(captions_path):
            subtitles = SubtitlesClip(captions_path, generator) # generator هي دالة تنسيق الخط
            final_video_bg = CompositeVideoClip([final_video_bg, subtitles.set_position(('center', 'center'))])

        # 6. دمج الصوت النهائي وتصدير الملف
        final_output = final_video_bg.set_audio(audio)
        output_file = "output/final.mp4"
        
        final_output.write_videofile(
            output_file,
            fps=30,
            codec="libx264",
            audio_codec="aac"
        )
        
        return output_file

    except Exception as e:
        print(f"Error during rendering: {e}")
        return None
