import json
import os

from config import HISTORY_FILE
from utils import confirm_action


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
            print("Invalid history format.")
            return {}

        return history

    except json.JSONDecodeError:
        print("History file is corrupted.")
        return {}

    except OSError:
        print("Could not read history file.")
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

    except OSError:
        print("Could not save history.")


def download_file_exists(download):
    file_path = download.get("file")

    if not file_path:
        return False

    return os.path.isfile(file_path)


def check_history(
    video_id,
    download_type,
    quality=None
):
    history = load_history()

    if video_id not in history:
        return True

    downloads = history[video_id].get(
        "downloads",
        []
    )

    for download in downloads:

        if download.get("type") != download_type:
            continue

        if download_type == "video":

            if download.get("quality") != quality:
                continue

        if download_file_exists(download):

            print("\nThis download already exists.")

            if download_type == "video":
                print(f"Quality: {quality}")

            print(
                f"File: {download.get('file')}"
            )

            return confirm_action(
                "Download again?"
            )

        else:
            print(
                "\nHistory found, but the actual "
                "file is missing."
            )

            print(
                "The download will be allowed again."
            )

            return True

    return True


def record_download(
    video_id,
    title,
    download_type,
    file_path,
    quality=None
):
    history = load_history()

    if video_id not in history:
        history[video_id] = {
            "title": title,
            "downloads": []
        }

    download_info = {
        "type": download_type,
        "file": os.path.abspath(file_path)
    }

    if quality:
        download_info["quality"] = quality

    history[video_id]["downloads"].append(
        download_info
    )

    save_history(history)


def display_history():
    history = load_history()

    if not history:
        print("\nNo download history found.")
        return

    print("\n========== DOWNLOAD HISTORY ==========")

    for video_id, video in history.items():

        print(f"\nTitle: {video.get('title', 'Unknown')}")
        print(f"Video ID: {video_id}")

        downloads = video.get(
            "downloads",
            []
        )

        for index, download in enumerate(
            downloads,
            start=1
        ):

            download_type = download.get(
                "type",
                "Unknown"
            )

            file_path = download.get(
                "file",
                "Unknown"
            )

            exists = download_file_exists(
                download
            )

            print(f"\n  Download {index}")
            print(f"  Type: {download_type}")

            if download_type == "video":
                print(
                    f"  Quality: "
                    f"{download.get('quality', 'Unknown')}"
                )

            print(
                f"  File: "
                f"{'Exists' if exists else 'Missing'}"
            )

            print(
                f"  Path: {file_path}"
            )

    print("\n=======================================")


def show_history():
    display_history()


def delete_history():
    history = load_history()

    if not history:
        print("\nNo download history found.")
        return

    video_ids = list(history.keys())

    print("\n========== HISTORY ==========")

    for index, video_id in enumerate(
        video_ids,
        start=1
    ):
        title = history[video_id].get(
            "title",
            "Unknown"
        )

        print(f"{index}. {title}")

    print(f"{len(video_ids) + 1}. Cancel")

    choice = input("\nChoose video to delete: ")

    if not choice.isdigit():
        print("Invalid choice.")
        return

    choice = int(choice)

    if choice == len(video_ids) + 1:
        return

    if not 1 <= choice <= len(video_ids):
        print("Invalid choice.")
        return

    video_id = video_ids[choice - 1]

    title = history[video_id].get(
        "title",
        "Unknown"
    )

    if confirm_action(
        f"Delete history for '{title}'?"
    ):
        del history[video_id]

        save_history(history)

        print("History deleted.")


def clear_all_history():
    history = load_history()

    if not history:
        print("\nNo download history found.")
        return

    if confirm_action(
        "Are you sure you want to clear ALL history?"
    ):
        save_history({})

        print("All history cleared.")


def history_manager():
    while True:

        print("\n==============================")
        print("       HISTORY MANAGER")
        print("==============================")
        print("1. View History")
        print("2. Delete History")
        print("3. Clear All History")
        print("4. Back")

        choice = input("\nEnter choice: ")

        if choice == "1":
            show_history()

        elif choice == "2":
            delete_history()

        elif choice == "3":
            clear_all_history()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")