import whisper


def generate_captions(audio_path):
    model = whisper.load_model("base")

    result = model.transcribe(audio_path)

    segments = result["segments"]

    with open("temp/captions.srt", "w", encoding="utf-8") as f:
        for i, segment in enumerate(segments):
            start = segment["start"]
            end = segment["end"]
            text = segment["text"]

            f.write(f"{i+1}\n")
            f.write(f"00:00:{start:05.2f} --> 00:00:{end:05.2f}\n")
            f.write(f"{text}\n\n")
