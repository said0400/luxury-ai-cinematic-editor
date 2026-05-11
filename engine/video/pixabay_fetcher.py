import requests
import random
import os
import logging

KEYWORDS = [
    "luxury aesthetic", "dark city night", "expensive car cinematic",
    "entrepreneur lifestyle", "abstract dark motion", "ocean waves dark",
    "expensive watch", "minimal architecture", "rainy window city"
]

def fetch_video(max_clips=5):
    api_key = os.getenv("PIXABAY_API_KEY")
    if not api_key:
        logging.error("Pixabay API Key missing!")
        return []

    downloaded_paths = []
    os.makedirs("temp/clips", exist_ok=True)

    # اختيار كلمات بحث متنوعة لضمان عدم التكرار
    selected_keywords = random.sample(KEYWORDS, k=max_clips)

    for i, keyword in enumerate(selected_keywords):
        try:
            url = f"https://pixabay.com/api/videos/?key={api_key}&q={keyword}&video_type=film&min_width=1080"
            response = requests.get(url).json()

            if not response.get("hits"):
                continue

            # اختيار فيديو عشوائي من النتائج الأولى (الأكثر صلة)
            hit = random.choice(response["hits"][:10])
            
            # محاولة الحصول على جودة HD أو Large
            video_url = hit["videos"].get("large", hit["videos"].get("medium"))["url"]
            
            logging.info(f"Downloading clip {i+1} for keyword: {keyword}...")
            video_data = requests.get(video_url, timeout=15).content

            clip_path = f"temp/clips/clip_{i}.mp4"
            with open(clip_path, "wb") as f:
                f.write(video_data)
            
            downloaded_paths.append(clip_path)

        except Exception as e:
            logging.error(f"Failed to fetch video for {keyword}: {e}")

    return downloaded_paths
