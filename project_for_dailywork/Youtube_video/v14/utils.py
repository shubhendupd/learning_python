import re
from urllib.parse import urlparse, parse_qs


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


def get_user_choice(prompt, options):
    while True:
        choice = input(prompt)

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(options):
                return choice

        print("Invalid choice. Please try again.")


def confirm_action(prompt):
    while True:
        answer = input(f"{prompt} (y/n): ").lower()

        if answer == "y":
            return True

        elif answer == "n":
            return False

        print("Please enter y or n.")


def sanitize_filename(filename):
    filename = re.sub(r'[<>:"/\\|?*]', "", filename)
    filename = filename.strip()
    filename = filename.rstrip(". ")

    if not filename:
        filename = "Unknown"

    return filename


def clean_youtube_url(url):
    parsed_url = urlparse(url)

    query = parse_qs(parsed_url.query)

    video_id = query.get("v")

    if not video_id:
        return url

    return f"https://www.youtube.com/watch?v={video_id[0]}"