from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_dynamic_video(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run without opening a browser
    options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-breakpad")
    options.add_argument("--disable-client-side-phishing-detection")
    options.add_argument("--disable-component-extensions-with-background-pages")
    options.add_argument("--disable-features=TranslateUI,BlinkGenPropertyTrees")
    options.add_argument("--disable-hang-monitor")
    options.add_argument("--disable-ipc-flooding-protection")
    options.add_argument("--disable-prompt-on-repost")
    options.add_argument("--disable-renderer-backgrounding")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-web-resources")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-webgl")
    options.add_argument("--disable-xss-auditor")
    options.add_argument("--enable-automation")
    options.add_argument("--log-level=0")
    options.add_argument("--no-first-run")
    options.add_argument("--no-service-autorun")
    options.add_argument("--password-store=basic")
    options.add_argument("--use-mock-keychain")
    options.add_argument("--user-data-dir=/tmp/user-data")
    options.add_argument("--v=99")
    options.add_argument("--single-process")
    options.add_argument("--data-path=/tmp/data-path")
    options.add_argument("--homedir=/tmp")
    options.add_argument("--disk-cache-dir=/tmp/cache-dir")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-accelerated-2d-canvas")
    options.add_argument("--disable-accelerated-jpeg-decoding")
    options.add_argument("--disable-accelerated-mjpeg-decode")
    options.add_argument("--disable-accelerated-video-decode")
    options.add_argument("--disable-accelerated-video-encode")

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
