from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def get_dynamic_video(url):
    # Set up Chrome options
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--disable-blink-features=AutomationControlled")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")  

    # Set up WebDriver
    service = Service("/usr/local/bin/chromedriver")  # Update this path
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(5)  # Allow page to load

        # ✅ For YouTube: Get the real video URL
        if "youtube.com" in url or "youtu.be" in url:
            video_element = driver.execute_script("return document.querySelector('video')")
            if video_element:
                video_url = video_element.get_attribute("src")
                return video_url if video_url else "YouTube Video URL not found."

        # ✅ For other platforms: Extract video tags
        video_elements = driver.find_elements(By.TAG_NAME, "video")
        video_links = [video.get_attribute("src") for video in video_elements if video.get_attribute("src")]

        return video_links if video_links else "No video found."

    except Exception as e:
        return f"Error: {str(e)}"

    finally:
        driver.quit()

# Example Usage
if __name__ == "__main__":
    video_url = input("Enter URL: ")
    print("Fetching dynamically loaded video...")
    print(get_dynamic_video(video_url))
