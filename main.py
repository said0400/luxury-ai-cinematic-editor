from engine.ai.script_generator import generate_script
from engine.audio.voice_generator import generate_voice
from engine.video.pixabay_fetcher import fetch_video
from engine.captions.captions import generate_captions
from engine.render.renderer import render_video


print("Generating cinematic script...")
script = generate_script()

print("Generating AI voice...")
generate_voice(script)

print("Downloading cinematic footage...")
fetch_video()

print("Generating captions...")
generate_captions("temp/voice.mp3")

print("Rendering final cinematic video...")
render_video()

print("Done.")
