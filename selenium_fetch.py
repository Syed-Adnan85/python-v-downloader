from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_dynamic_video(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run without opening a browser
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(5)  # Wait for content to load

    video_elements = driver.find_elements(By.TAG_NAME, "video")
    video_links = [video.get_attribute("src") for video in video_elements if video.get_attribute("src")]

    driver.quit()
    return video_links

# Example Usage
if __name__ == "__main__":
    video_url = input("Enter URL: ")
    print("Fetching dynamically loaded video...")
    print(get_dynamic_video(video_url))
