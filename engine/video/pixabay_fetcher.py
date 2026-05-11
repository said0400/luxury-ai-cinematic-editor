import requests
import random
import os


KEYWORDS = [
    "luxury",
    "night city",
    "supercar",
    "businessman",
    "dark cinematic",
    "success",
    "wealth"
]


def fetch_video():
    api_key = os.getenv("PIXABAY_API_KEY")

    keyword = random.choice(KEYWORDS)

    url = f"https://pixabay.com/api/videos/?key={api_key}&q={keyword}"

    response = requests.get(url).json()

    hit = random.choice(response["hits"])

    video_url = hit["videos"]["large"]["url"]

    video_data = requests.get(video_url).content

    with open("temp/clip.mp4", "wb") as f:
        f.write(video_data)
