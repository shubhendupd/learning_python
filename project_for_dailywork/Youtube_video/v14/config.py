import os


BROWSER = "firefox"

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))

VIDEO_FOLDER = os.path.join(
    BASE_FOLDER,
    "downloads",
    "videos"
)

AUDIO_FOLDER = os.path.join(
    BASE_FOLDER,
    "downloads",
    "audio"
)

HISTORY_FILE = os.path.join(
    BASE_FOLDER,
    "history.json"
)


COMMON_OPTIONS = {
    "cookiesfrombrowser": (BROWSER,),
    "remote_components": ["ejs:github"],
    "noplaylist": True,
}