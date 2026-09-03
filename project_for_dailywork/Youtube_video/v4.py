import yt_dlp
import os


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

        available_qualities = sorted(available_qualities, reverse=True)

        if not available_qualities:
            print("No H.264 MP4 video formats found.")
            return

        print("\nAvailable H.264 qualities:")

        for index, height in enumerate(available_qualities, start=1):
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

        print(f"\nDownloading {quality}p...")

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
        print("2. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            download_video()

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()