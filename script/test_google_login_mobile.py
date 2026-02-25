import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ── 設定 ──────────────────────────────────────────────
# 改用自訂尺寸，避免 Chrome 版本更新後 device name 失效
MOBILE_DEVICE = {
    "deviceMetrics": {"width": 393, "height": 851, "pixelRatio": 2.75, "touch": True},
    "userAgent": (
        "Mozilla/5.0 (Linux; Android 11; Pixel 5) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/144.0.0.0 Mobile Safari/537.36"
    ),
}
TARGET_URL     = "https://xyz-beta.protago-dev.com/home"
GOOGLE_EMAIL   = "xyzdev02@cqigames.com"
GOOGLE_PASSWORD = "Abc123123?"
# ──────────────────────────────────────────────────────


def _create_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", MOBILE_DEVICE)
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    selenium_url = os.getenv("SELENIUM_REMOTE_URL")
    if selenium_url:
        return webdriver.Remote(command_executor=selenium_url, options=options)
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def test_google_login_mobile():
    driver = _create_driver()
    wait = WebDriverWait(driver, 15)

    try:
        # ── Step 0: 清除 session，確保未登入狀態 ──────────────
        print("\n📍 Step 0: 清除 cookies & storage")
        driver.get(TARGET_URL)
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        driver.delete_all_cookies()
        driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
        driver.get(TARGET_URL)
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        time.sleep(2)
        print(f"   URL: {driver.current_url}")

        # ── Step 1: 觸發登入 popup（首頁已無直接 Login 按鈕）────
        # 按下 Start Chatting 或 Create Agent 會彈出登入 popup
        print("📍 Step 1: 觸發登入 popup")
        trigger_selectors = [
            (By.XPATH, "//*[contains(text(), 'Start Chatting')]"),
            (By.XPATH, "//*[contains(text(), 'Start chatting')]"),
            (By.XPATH, "//*[contains(text(), 'Create Agent')]"),
            (By.XPATH, "//*[contains(text(), 'Create agent')]"),
            # 舊版 fallback
            (By.XPATH, "//*[normalize-space(text())='Sign Up / Log In']"),
            (By.XPATH, "//*[contains(text(), 'Log In')]"),
            (By.XPATH, "//*[contains(text(), 'Log in')]"),
        ]
        clicked = False
        for by, sel in trigger_selectors:
            try:
                btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((by, sel)))
                btn.click()
                print(f"   ✅ 已點擊: {sel}")
                clicked = True
                break
            except Exception:
                continue
        if not clicked:
            driver.save_screenshot("debug_login_btn_not_found.png")
            raise Exception("找不到觸發登入的按鈕，截圖已存 debug_login_btn_not_found.png")
        time.sleep(2)

        # ── Step 2: 點擊 Google 登入按鈕 ─────────────────────
        print("📍 Step 2: 點擊 Google 登入按鈕")
        google_selectors = [
            (By.XPATH, "//button[contains(., 'Google')]"),
            (By.XPATH, "//div[contains(., 'Continue with Google') and @role='button']"),
            (By.XPATH, "//*[contains(text(), 'Continue with Google')]"),
            (By.XPATH, "//*[contains(text(), 'Google')]"),
            (By.CSS_SELECTOR, "[class*='google']"),
        ]
        main_window = driver.current_window_handle
        clicked = False
        for by, sel in google_selectors:
            try:
                btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((by, sel)))
                btn.click()
                print(f"   ✅ 已點擊: {sel}")
                clicked = True
                break
            except Exception:
                continue
        if not clicked:
            driver.save_screenshot("debug_google_btn_not_found.png")
            raise Exception("找不到 Google 登入按鈕，截圖已存 debug_google_btn_not_found.png")
        time.sleep(3)

        # ── Step 3: 判斷 popup 或 redirect ────────────────────
        all_windows = driver.window_handles
        if len(all_windows) > 1:
            google_window = [w for w in all_windows if w != main_window][0]
            driver.switch_to.window(google_window)
            print(f"📍 Step 3: 偵測到 popup，已切換 (handles: {len(all_windows)})")
        else:
            print("📍 Step 3: redirect 模式（同一分頁）")
        print(f"   Google URL: {driver.current_url}")
        time.sleep(2)

        # ── Step 4: 輸入 Google Email ─────────────────────────
        print("📍 Step 4: 輸入 Google Email")
        email_input = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='email']"))
        )
        email_input.clear()
        email_input.send_keys(GOOGLE_EMAIL)
        time.sleep(0.5)

        next_btn = wait.until(EC.element_to_be_clickable((By.ID, "identifierNext")))
        next_btn.click()
        print("   ✅ Email 送出")
        time.sleep(2)

        # ── Step 5: 輸入 Google 密碼 ─────────────────────────
        print("📍 Step 5: 輸入 Google 密碼")
        password_input = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']"))
        )
        password_input.clear()
        password_input.send_keys(GOOGLE_PASSWORD)
        time.sleep(0.5)

        pass_next_btn = wait.until(EC.element_to_be_clickable((By.ID, "passwordNext")))
        pass_next_btn.click()
        print("   ✅ 密碼送出")
        time.sleep(3)

        # ── Step 6: 切回主視窗（popup 模式）─────────────────
        if len(driver.window_handles) > 1:
            driver.switch_to.window(main_window)
            print("📍 Step 6: 切回 XYZ 主視窗")

        # ── Step 7: 驗證登入成功 ──────────────────────────────
        print("📍 Step 7: 驗證登入成功")
        WebDriverWait(driver, 30).until(
            lambda d: (
                len(d.find_elements(By.XPATH, "//span[contains(text(), 'Agent')]")) > 0
                or len(d.find_elements(By.XPATH, "//*[contains(@class, 'avatar')]")) > 0
                or "/home" in d.current_url
            )
        )
        print(f"   ✅ 登入成功！URL: {driver.current_url}")
        driver.save_screenshot("google_login_mobile_success.png")

    except Exception as e:
        print(f"\n❌ 測試失敗: {e}")
        driver.save_screenshot("google_login_mobile_error.png")
        raise

    finally:
        driver.quit()


if __name__ == "__main__":
    test_google_login_mobile()
