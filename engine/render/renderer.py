from moviepy.editor import *
from engine.video.effects import apply_effects


def render_video():
    video = VideoFileClip("temp/clip.mp4")

    audio = AudioFileClip("temp/voice.mp3")

    video = video.subclip(0, audio.duration)

    video = video.resize((1080, 1920))

    video = apply_effects(video)

    final = video.set_audio(audio)

    final.write_videofile(
        "output/final.mp4",
        fps=60,
        codec="libx264",
        audio_codec="aac",
        preset="slow",
        threads=4
    )
