from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

def test_google_title():
    selenium_url = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless=new")

    driver = webdriver.Remote(command_executor=selenium_url, options=options)

    print("🚀 開始載入頁面...")
    driver.get("https://xyz-beta.protago-dev.com/home")
    time.sleep(3)
    print("📍 Current URL:", driver.current_url)
    print("📍 Title:", driver.title)
    print("📍 First 500 chars of page:", driver.page_source[:500])

    assert "NetMind XYZ" in driver.title
    driver.quit()