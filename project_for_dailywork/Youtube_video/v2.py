import yt_dlp

url = input("Enter YouTube URL: ")
quality = input("Choose quality (360p, 480p, 720p, 1080p): ")

quality = quality.replace("p", "")

options = {
    "format": f"bestvideo[height<={quality}][vcodec^=avc1]+bestaudio[ext=m4a]/best[height<={quality}]",
    "outtmpl": "downloads/%(title)s.%(ext)s",
    "cookiesfrombrowser": ("firefox",),
    "remote_components": ["ejs:github"],
    "merge_output_format": "mp4",
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])