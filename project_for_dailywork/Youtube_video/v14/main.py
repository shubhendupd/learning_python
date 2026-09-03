import os

from config import VIDEO_FOLDER, AUDIO_FOLDER

from downloader import (
    download_video,
    download_audio
)

from history import history_manager

from utils import get_user_choice


def create_folders():
    os.makedirs(
        VIDEO_FOLDER,
        exist_ok=True
    )

    os.makedirs(
        AUDIO_FOLDER,
        exist_ok=True
    )


def main():
    create_folders()

    options = [
        "Download Video",
        "Download Audio",
        "History Manager",
        "Exit"
    ]

    while True:

        print("\n================================")
        print("       YOUTUBE DOWNLOADER")
        print("================================")

        for index, option in enumerate(
            options,
            start=1
        ):
            print(f"{index}. {option}")

        choice = get_user_choice(
            "\nEnter choice: ",
            options
        )

        if choice == 1:
            download_video()

        elif choice == 2:
            download_audio()

        elif choice == 3:
            history_manager()

        elif choice == 4:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()