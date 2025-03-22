from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fetch_video import get_video_info
from selenium_fetch import get_dynamic_video

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def home():
    return {"message": "Welcome to the Universal Video Fetcher API!"}

@app.get("/fetch/")
def fetch_video(url: str):
    try:
        video_info = get_video_info(url)
        if video_info:
            return {"status": "success", "data": video_info}
    except Exception as e:
        print("yt-dlp failed, trying Selenium...")

    try:
        dynamic_urls = get_dynamic_video(url)
        if dynamic_urls:
            return {"status": "success", "video_urls": dynamic_urls}
    except Exception as e:
        return {"status": "error", "message": str(e)}

    return {"status": "error", "message": "Could not fetch video."}

@app.get("/fetch_dash/")
def fetch_dash_video(url: str):
    try:
        video_info = get_video_info(url, dash=True)
        if video_info:
            return {"status": "success", "data": video_info}
    except Exception as e:
        return {"status": "error", "message": str(e)}

    return {"status": "error", "message": "Could not fetch DASH video."}
