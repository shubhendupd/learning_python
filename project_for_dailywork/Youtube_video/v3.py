import yt_dlp
import os

def download_video():
    url = input("\nEnter YouTube URL: ")

    print("\nChoose video quality: ")
    print("1. 1080p")
    print("2. 720p")
    print("3. 480p")
    print("4. 360p")

    choice = input("\nEnter your choice (1-4): ")

    quality_map = {
        "1": "1080",
        "2": "720",
        "3": "480",
        "4": "360"
    }

    if choice not in quality_map:
        print("Invalid quality choice.")
        return

    quality = quality_map[choice]

    options = {
        "format": (
            f"bestvideo[height<={quality}][ext=mp4][vcodec^=avc1]"
            f"+bestaudio[ext=m4a]/"
            f"best[height<={quality}]"
        ),
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "cookiesfrombrowser": ("firefox",),
        "remote_components": ["ejs:github"],
        "merge_output_format": "mp4",
    }
    

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        print("\nDownload completed successfully.")

    except yt_dlp.utils.DownloadError as e:
        print(f"\nError downloading video: {e}")

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
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()