import yt_dlp
import os

def download_audio():
    url = input("\nEnter YouTube URL: ")

    try:
        print("\nDownloading audio...\n")

        options = {
            "format": "bestaudio/best",

            "outtmpl": "downloads/%(title)s.%(ext)s",

            "cookiesfrombrowser": ("firefox",),

            "remote_components": ["ejs:github"],

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

        print("\nAudio download completed successfully!")

    except yt_dlp.utils.DownloadError as e:

        print("\nAudio download failed.")
        print(f"Error: {e}")


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
        print("\nProcessing video...")


def get_video_info(url):
    options = {
        "cookiesfrombrowser": ("firefox",),
        "remote_components": ["ejs:github"],
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        return ydl.extract_info(url, download=False)


def download_video():

    url = input("\nEnter YouTube URL: ")

    try:
        print("\nChecking available formats...")

        info = get_video_info(url)

        formats = info.get("formats", [])

        available_qualities = set()

        for format in formats:

            if (
                format.get("vcodec", "").startswith("avc1")
                and format.get("ext") == "mp4"
                and format.get("height")
            ):
                available_qualities.add(format["height"])

        available_qualities = sorted(
            available_qualities,
            reverse=True
        )

        if not available_qualities:
            print("No H.264 MP4 video formats found.")
            return

        print("\nAvailable H.264 qualities:")

        for index, height in enumerate(
            available_qualities,
            start=1
        ):
            print(f"{index}. {height}p")

        choice = input("\nChoose quality: ")

        if not choice.isdigit():
            print("Please enter a number.")
            return

        choice = int(choice)

        if choice < 1 or choice > len(available_qualities):
            print("Invalid choice.")
            return

        quality = available_qualities[choice - 1]

        print(f"\nDownloading {quality}p...\n")

        options = {
            "format": (
                f"bestvideo[height<={quality}]"
                f"[ext=mp4][vcodec^=avc1]"
                f"+bestaudio[ext=m4a]/"
                f"best[height<={quality}]"
            ),

            "outtmpl": "downloads/%(title)s.%(ext)s",

            "cookiesfrombrowser": ("firefox",),

            "remote_components": ["ejs:github"],

            "merge_output_format": "mp4",

            "progress_hooks": [progress_hook],
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        print("\nDownload completed successfully!")

    except yt_dlp.utils.DownloadError as e:

        print("\nDownload failed.")
        print(f"Error: {e}")


def main():

    os.makedirs("downloads", exist_ok=True)

    while True:

        print("\n================================")
        print("       YOUTUBE DOWNLOADER")
        print("================================")
        print("1. Download Video")
        print("2. Download Audio")
        print("3. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            download_video()

        elif choice == "2":
            download_audio()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if main() == "__main__":
    main()