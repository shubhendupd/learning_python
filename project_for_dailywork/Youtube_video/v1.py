import yt_dlp

url = input("Enter YouTube URL: ")

options = {
    "outtmpl": "downloads/%(title)s.%(ext)s",
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])