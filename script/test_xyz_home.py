import time
from selenium.webdriver.common.by import By

TARGET_URL = "https://xyz-beta.protago-dev.com/home"


def test_xyz_home_title(web_driver):
    driver = web_driver
    print("🚀 開始載入頁面...")
    driver.get(TARGET_URL)
    time.sleep(3)
    print("📍 Current URL:", driver.current_url)
    print("📍 Title:", driver.title)
    print("📍 First 500 chars of page:", driver.page_source[:500])
    assert "NetMind XYZ" in driver.title
