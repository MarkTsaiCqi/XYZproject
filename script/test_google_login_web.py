import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TARGET_URL       = "https://xyz-beta.protago-dev.com/home"
_GOOGLE_EMAIL    = "xyzdev02@cqigames.com"
_GOOGLE_PASSWORD = "Abc123123?"   # 不印出，僅供 send_keys 使用


def test_google_login_web(web_driver):
    """Google OAuth 桌面版登入流程（1920x1080 desktop Chrome）"""
    driver = web_driver
    wait   = WebDriverWait(driver, 15)

    # ── Step 0: 清除 session ──────────────────────────────────────────────────
    print("\n📍 Step 0: 清除 cookies & storage")
    driver.get(TARGET_URL)
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
    driver.get(TARGET_URL)
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
    time.sleep(2)
    print(f"   URL: {driver.current_url}")

    # ── Step 1: 觸發登入 popup ────────────────────────────────────────────────
    print("📍 Step 1: 觸發登入 popup")
    trigger_selectors = [
        (By.XPATH, "//*[contains(text(), 'Start Chatting')]"),
        (By.XPATH, "//*[contains(text(), 'Start chatting')]"),
        (By.XPATH, "//*[contains(text(), 'Create Agent')]"),
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
        raise AssertionError("找不到觸發登入的按鈕")
    time.sleep(2)

    # ── Step 2: 點擊 Google 登入按鈕 ─────────────────────────────────────────
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
        raise AssertionError("找不到 Google 登入按鈕")
    time.sleep(3)

    # ── Step 3: 切換視窗（popup 或 redirect）────────────────────────────────
    all_windows = driver.window_handles
    if len(all_windows) > 1:
        google_window = [w for w in all_windows if w != main_window][0]
        driver.switch_to.window(google_window)
        print(f"📍 Step 3: popup 模式，已切換 (handles: {len(all_windows)})")
    else:
        print("📍 Step 3: redirect 模式（同一分頁）")
    print(f"   Google URL: {driver.current_url}")
    time.sleep(2)

    # ── Step 4: 輸入 Google Email ─────────────────────────────────────────────
    print("📍 Step 4: 輸入 Google Email")
    email_input = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='email']"))
    )
    email_input.clear()
    email_input.send_keys(_GOOGLE_EMAIL)
    time.sleep(0.5)
    wait.until(EC.element_to_be_clickable((By.ID, "identifierNext"))).click()
    print("   ✅ Email 送出")
    time.sleep(2)

    # ── Step 5: 輸入 Google 密碼 ──────────────────────────────────────────────
    print("📍 Step 5: 輸入 Google 密碼")
    password_input = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']"))
    )
    password_input.clear()
    password_input.send_keys(_GOOGLE_PASSWORD)
    time.sleep(0.5)
    wait.until(EC.element_to_be_clickable((By.ID, "passwordNext"))).click()
    print("   ✅ 密碼送出")
    time.sleep(3)

    # ── Step 6: 切回主視窗（popup 模式）──────────────────────────────────────
    if len(driver.window_handles) > 1:
        driver.switch_to.window(main_window)
        print("📍 Step 6: 切回 XYZ 主視窗")

    # ── Step 7: 驗證登入成功 ──────────────────────────────────────────────────
    print("📍 Step 7: 驗證登入成功")
    WebDriverWait(driver, 30).until(
        lambda d: (
            d.current_url != TARGET_URL
            or len(d.find_elements(By.XPATH, "//span[contains(text(), 'Agent')]")) > 0
            or len(d.find_elements(By.XPATH, "//*[contains(@class, 'avatar')]")) > 0
        )
    )
    assert "login" not in driver.current_url.lower(), f"登入失敗，停在登入頁: {driver.current_url}"
    print(f"   ✅ 登入成功！URL: {driver.current_url}")
