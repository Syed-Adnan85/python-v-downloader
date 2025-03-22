import yt_dlp

def get_video_info(url):
    ydl_opts = {
        'quiet': True,
        'format': 'best',
        'noplaylist': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    video_info = {
        "title": info.get("title"),
        "thumbnail": info.get("thumbnail"),
        "watch_url": info.get("webpage_url"),
        "formats": [
            {
                "format_id": f["format_id"],
                "quality": f["format"],
                "url": f["url"]
            }
            for f in info.get("formats", [])
        ]
    }
    
    return video_info
