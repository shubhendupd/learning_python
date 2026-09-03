import os
import yt_dlp

from config import (
    COMMON_OPTIONS,
    VIDEO_FOLDER,
    AUDIO_FOLDER
)

from utils import (
    progress_hook,
    get_user_choice,
    confirm_action,
    sanitize_filename,
    clean_youtube_url
)

from history import (
    check_history,
    record_download
)


def get_video_info(url):
    options = {
        **COMMON_OPTIONS,
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(
            url,
            download=False
        )
 # print("\n========== FORMATS ==========")

        # for format in info.get("formats", []):
        #     print(
        #         format.get("format_id"),
        #         format.get("ext"),
        #         format.get("height"),
        #         format.get("vcodec")
        #     )

        # print("==============================")
        return info


def download_video():
    url = input("Enter YouTube URL: ")

    # Remove playlist parameters
    url = clean_youtube_url(url)

    print("\nChecking available formats...")

    info = get_video_info(url)

    title = info["title"]
    video_id = info["id"]

    formats = []

    for format in info.get("formats", []):
        if (
            format.get("vcodec", "").startswith("avc1")
            and format.get("ext") == "mp4"
            and format.get("height")
        ):
            formats.append(format)

    qualities = sorted(
        set(format["height"] for format in formats),
        reverse=True
    )

    if not qualities:
        print("No H.264 MP4 video formats found.")
        return

    print("\nAvailable H.264 qualities:")

    for index, quality in enumerate(qualities, start=1):
        print(f"{index}. {quality}p")

    choice = get_user_choice(
        "\nChoose quality: ",
        qualities
    )

    quality = qualities[choice - 1]

    # Check history before downloading
    if not check_history(
        video_id,
        "video",
        f"{quality}p"
    ):
        return

    if not confirm_action(
        f"Download {quality}p video?"
    ):
        print("Download cancelled.")
        return

    safe_title = sanitize_filename(title)

    options = {
        **COMMON_OPTIONS,
        "format": (
            f"bestvideo[height<={quality}]"
            f"[ext=mp4][vcodec^=avc1]"
            f"+bestaudio[ext=m4a]/"
            f"best[height<={quality}]"
        ),
        "merge_output_format": "mp4",
        "outtmpl": f"{VIDEO_FOLDER}/{safe_title}.%(ext)s",
        "progress_hooks": [progress_hook],
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

    file_path = os.path.join(
        VIDEO_FOLDER,
        f"{safe_title}.mp4"
    )

    record_download(
        video_id,
        title,
        "video",
        file_path,
        f"{quality}p"
    )

    print("\nVideo download completed!")


def download_audio():
    url = input("Enter YouTube URL: ")

    # Remove playlist parameters
    url = clean_youtube_url(url)

    print("\nGetting video information...")

    info = get_video_info(url)

    title = info["title"]
    video_id = info["id"]

    # Check history before downloading
    if not check_history(
        video_id,
        "audio"
    ):
        return

    if not confirm_action("Download audio?"):
        print("Download cancelled.")
        return

    safe_title = sanitize_filename(title)

    options = {
        **COMMON_OPTIONS,
        "format": "bestaudio/best",
        "outtmpl": f"{AUDIO_FOLDER}/{safe_title}.%(ext)s",
        "progress_hooks": [progress_hook],
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

    file_path = os.path.join(
        AUDIO_FOLDER,
        f"{safe_title}.mp3"
    )

    record_download(
        video_id,
        title,
        "audio",
        file_path
    )

    print("\nAudio download completed!")