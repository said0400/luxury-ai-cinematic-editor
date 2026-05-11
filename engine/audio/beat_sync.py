import librosa
import numpy as np
import logging

def analyze_beats(audio_path):
    try:
        # 1. تحميل الملف مع تحديد التردد (Sampling Rate) لتسريع العملية
        # نكتفي بـ 60 ثانية لتقليل استهلاك الذاكرة
        y, sr = librosa.load(audio_path, sr=22050, duration=60)

        # 2. تحسين الدقة عبر تحليل قوة البدايات (Onset Strength)
        onset_env = librosa.onset.onset_strength(y=y, sr=sr)
        
        # 3. تتبع الإيقاع بناءً على قوة البدايات
        tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)

        # 4. تحويل الفريمات إلى توقيتات بالثواني
        beat_times = librosa.frames_to_time(beats, sr=sr)

        # إضافة توقيت 0 في البداية لضمان وجود نقطة انطلاق للمشاهد
        if len(beat_times) > 0 and beat_times[0] > 0.5:
            beat_times = np.insert(beat_times, 0, 0.0)

        logging.info(f"Detected Tempo: {tempo:.2f} BPM | Found {len(beat_times)} beats.")
        return beat_times.tolist()

    except Exception as e:
        logging.error(f"Error analyzing audio: {e}")
        return []
