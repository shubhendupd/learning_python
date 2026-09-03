import yt_dlp
import os
import json


# ==============================
# CONFIGURATION
# ==============================

BROWSER = "firefox"

VIDEO_FOLDER = "downloads/videos"
AUDIO_FOLDER = "downloads/audio"

HISTORY_FILE = "history.json"

COMMON_OPTIONS = {
    "cookiesfrombrowser": (BROWSER,),
    "remote_components": ["ejs:github"],
}


# ==============================
# PROGRESS
# ==============================

def progress_hook(data):

    if data["status"] == "downloading":

        percent = data.get("_percent_str", "N/A")
        speed = data.get("_speed_str", "N/A")
        eta = data.get("_eta_str", "N/A")

        print(
            f"\rDownloading: {percent} | "
            f"Speed: {speed} | "
            f"ETA: {eta}",
            end=""
        )

    elif data["status"] == "finished":

        print("\nProcessing...")


# ==============================
# HISTORY
# ==============================

def load_history():

    if not os.path.exists(HISTORY_FILE):

        return {}

    try:

        with open(
            HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            history = json.load(file)

            if not isinstance(history, dict):

                print(
                    "\nHistory file contains invalid data."
                )

                return {}

            return history

    except json.JSONDecodeError:

        print(
            "\nHistory file contains invalid JSON."
        )

        print(
            "Starting with empty history."
        )

        return {}

    except OSError as e:

        print(
            f"\nCould not read history file: {e}"
        )

        return {}


def save_history(history):

    try:

        with open(
            HISTORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                indent=4,
                ensure_ascii=False
            )

    except OSError as e:

        print(
            f"\nCould not save history: {e}"
        )


def check_history(
    video_id,
    download_type,
    quality=None
):

    history = load_history()

    if video_id not in history:

        return True

    video_history = history[video_id]

    downloads = video_history.get(
        "downloads",
        []
    )

    for download in downloads:

        if (
            download["type"] == download_type
            and download.get("quality") == quality
        ):

            print(
                "\nThis download already exists."
            )

            print(
                f"Title: {video_history['title']}"
            )

            if quality:

                print(
                    f"Quality: {quality}"
                )

            print(
                f"Type: {download_type}"
            )

            choice = input(
                "Download again? (y/n): "
            ).lower()

            return choice == "y"

    return True


def record_download(
    video_id,
    title,
    download_type,
    quality=None
):

    history = load_history()

    if video_id not in history:

        history[video_id] = {
            "title": title,
            "downloads": []
        }

    download_info = {
        "type": download_type
    }

    if quality:

        download_info["quality"] = quality

    history[video_id]["downloads"].append(
        download_info
    )

    save_history(history)


# ==============================
# VIEW HISTORY
# ==============================

def show_history():

    history = load_history()

    if not history:

        print(
            "\nNo download history found."
        )

        return

    print(
        "\n========== DOWNLOAD HISTORY =========="
    )

    for index, (video_id, video_data) in enumerate(
        history.items(),
        start=1
    ):

        print(
            f"\n{index}. {video_data['title']}"
        )

        for download in video_data["downloads"]:

            if download["type"] == "video":

                print(
                    f"   Video: {download['quality']}"
                )

            elif download["type"] == "audio":

                print(
                    "   Audio: MP3"
                )

    print(
        "\n======================================"
    )


# ==============================
# DELETE HISTORY
# ==============================

def delete_history():

    history = load_history()

    if not history:

        print(
            "\nNo download history found."
        )

        return

    print(
        "\n========== DOWNLOAD HISTORY =========="
    )

    history_items = list(
        history.items()
    )

    for index, (video_id, video_data) in enumerate(
        history_items,
        start=1
    ):

        print(
            f"{index}. {video_data['title']}"
        )

    print(
        "\n======================================"
    )

    choice = input(
        "\nEnter number to delete: "
    )

    if not choice.isdigit():

        print(
            "Please enter a number."
        )

        return

    choice = int(choice)

    if (
        choice < 1
        or choice > len(history_items)
    ):

        print(
            "Invalid choice."
        )

        return

    video_id = history_items[
        choice - 1
    ][0]

    title = history[video_id]["title"]

    print(
        f"\nSelected: {title}"
    )

    confirmation = input(
        "Are you sure you want to delete "
        "this history? (y/n): "
    ).lower()

    if confirmation != "y":

        print(
            "Deletion cancelled."
        )

        return

    del history[video_id]

    save_history(history)

    print(
        "\nHistory deleted successfully."
    )


# ==============================
# CLEAR ALL HISTORY
# ==============================

def clear_all_history():

    history = load_history()

    if not history:

        print(
            "\nNo download history found."
        )

        return

    print(
        f"\nYou have {len(history)} "
        "history entries."
    )

    confirmation = input(
        "Delete ALL history? (y/n): "
    ).lower()

    if confirmation != "y":

        print(
            "Deletion cancelled."
        )

        return

    save_history({})

    print(
        "\nAll history deleted successfully."
    )


# ==============================
# HISTORY MANAGER
# ==============================

def history_manager():

    while True:

        print(
            "\n================================"
        )

        print(
            "        HISTORY MANAGER"
        )

        print(
            "================================"
        )

        print(
            "1. View History"
        )

        print(
            "2. Delete History"
        )

        print(
            "3. Clear All History"
        )

        print(
            "4. Back"
        )

        choice = input(
            "\nEnter choice: "
        )

        if choice == "1":

            show_history()

        elif choice == "2":

            delete_history()

        elif choice == "3":

            clear_all_history()

        elif choice == "4":

            break

        else:

            print(
                "Invalid choice."
            )


# ==============================
# VIDEO INFORMATION
# ==============================

def get_video_info(url):

    options = {
        **COMMON_OPTIONS,
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(options) as ydl:

        return ydl.extract_info(
            url,
            download=False
        )


# ==============================
# DOWNLOAD VIDEO
# ==============================

def download_video():

    url = input(
        "\nEnter YouTube URL: "
    )

    try:

        print(
            "\nChecking available formats..."
        )

        info = get_video_info(url)

        video_id = info["id"]

        title = info.get(
            "title",
            "Unknown"
        )

        formats = info.get(
            "formats",
            []
        )

        available_qualities = set()

        for format in formats:

            if (
                format.get(
                    "vcodec",
                    ""
                ).startswith("avc1")
                and format.get("ext") == "mp4"
                and format.get("height")
            ):

                available_qualities.add(
                    format["height"]
                )

        available_qualities = sorted(
            available_qualities,
            reverse=True
        )

        if not available_qualities:

            print(
                "No H.264 MP4 video formats found."
            )

            return

        print(
            "\nAvailable H.264 qualities:"
        )

        for index, height in enumerate(
            available_qualities,
            start=1
        ):

            print(
                f"{index}. {height}p"
            )

        choice = input(
            "\nChoose quality: "
        )

        if not choice.isdigit():

            print(
                "Please enter a number."
            )

            return

        choice = int(choice)

        if (
            choice < 1
            or choice > len(
                available_qualities
            )
        ):

            print(
                "Invalid choice."
            )

            return

        quality = available_qualities[
            choice - 1
        ]

        quality_text = f"{quality}p"

        if not check_history(
            video_id,
            "video",
            quality_text
        ):

            print(
                "Download cancelled."
            )

            return

        print(
            f"\nDownloading {quality_text}...\n"
        )

        options = {

            **COMMON_OPTIONS,

            "format": (
                f"bestvideo[height<={quality}]"
                f"[ext=mp4][vcodec^=avc1]"
                f"+bestaudio[ext=m4a]/"
                f"best[height<={quality}]"
            ),

            "outtmpl": (
                f"{VIDEO_FOLDER}/"
                "%(title)s.%(ext)s"
            ),

            "merge_output_format": "mp4",

            "progress_hooks": [
                progress_hook
            ],
        }

        with yt_dlp.YoutubeDL(
            options
        ) as ydl:

            ydl.download([url])

        record_download(
            video_id,
            title,
            "video",
            quality_text
        )

        print(
            "\nDownload completed successfully!"
        )

    except yt_dlp.utils.DownloadError as e:

        print(
            "\nDownload failed."
        )

        print(
            f"Error: {e}"
        )


# ==============================
# DOWNLOAD AUDIO
# ==============================

def download_audio():

    url = input(
        "\nEnter YouTube URL: "
    )

    try:

        print(
            "\nChecking video..."
        )

        info = get_video_info(url)

        video_id = info["id"]

        title = info.get(
            "title",
            "Unknown"
        )

        if not check_history(
            video_id,
            "audio"
        ):

            print(
                "Download cancelled."
            )

            return

        print(
            "\nDownloading audio...\n"
        )

        options = {

            **COMMON_OPTIONS,

            "format": "bestaudio/best",

            "outtmpl": (
                f"{AUDIO_FOLDER}/"
                "%(title)s.%(ext)s"
            ),

            "progress_hooks": [
                progress_hook
            ],

            "postprocessors": [

                {
                    "key":
                        "FFmpegExtractAudio",

                    "preferredcodec":
                        "mp3",

                    "preferredquality":
                        "192",
                }

            ],
        }

        with yt_dlp.YoutubeDL(
            options
        ) as ydl:

            ydl.download([url])

        record_download(
            video_id,
            title,
            "audio"
        )

        print(
            "\nAudio download completed successfully!"
        )

    except yt_dlp.utils.DownloadError as e:

        print(
            "\nAudio download failed."
        )

        print(
            f"Error: {e}"
        )


# ==============================
# MAIN MENU
# ==============================

def main():

    os.makedirs(
        VIDEO_FOLDER,
        exist_ok=True
    )

    os.makedirs(
        AUDIO_FOLDER,
        exist_ok=True
    )

    while True:

        print(
            "\n================================"
        )

        print(
            "       YOUTUBE DOWNLOADER"
        )

        print(
            "================================"
        )

        print(
            "1. Download Video"
        )

        print(
            "2. Download Audio"
        )

        print(
            "3. History Manager"
        )

        print(
            "4. Exit"
        )

        choice = input(
            "\nEnter choice: "
        )

        if choice == "1":

            download_video()

        elif choice == "2":

            download_audio()

        elif choice == "3":

            history_manager()

        elif choice == "4":

            print(
                "Goodbye!"
            )

            break

        else:

            print(
                "Invalid choice."
            )


# ==============================
# PROGRAM START
# ==============================

if __name__ == "__main__":

    main()