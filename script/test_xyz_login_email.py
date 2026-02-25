import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TARGET_URL = "https://xyz-beta.protago-dev.com/home"
_EMAIL    = "xyzdev01@cqigames.com"
_PASSWORD = "Abc123123?"   # 不印出，僅供 send_keys 使用


def test_xyz_login_email(web_driver):
    """Email 登入流程"""
    driver = web_driver
    wait   = WebDriverWait(driver, 15)

    # ── Step 0: 清除 session ──────────────────────────────────────────────────
    print("📍 Step 0: 清除 cookies & storage")
    driver.get(TARGET_URL)
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
    driver.get(TARGET_URL)
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
    time.sleep(2)
    print(f"   URL: {driver.current_url}")
    print(f"   Title: {driver.title}")

    # ── Step 1: 觸發登入 popup ────────────────────────────────────────────────
    print("📍 Step 1: 觸發登入 popup")
    trigger_selectors = [
        (By.XPATH, "//*[contains(text(), 'Start Chatting')]"),
        (By.XPATH, "//*[contains(text(), 'Start chatting')]"),
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

    # ── Step 2: 輸入 Email ────────────────────────────────────────────────────
    print("📍 Step 2: 輸入 Email")
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='example@site.com']"))
    )
    email_input.clear()
    email_input.send_keys(_EMAIL)
    print(f"   ✅ Email 已輸入: {_EMAIL}")
    time.sleep(1)

    # ── Step 3: 點擊下一步 ────────────────────────────────────────────────────
    print("📍 Step 3: 點擊下一步")
    try:
        next_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ant-btn-primary .anticon-arrow-right"))
        )
        next_btn.click()
    except Exception:
        driver.find_element(By.CSS_SELECTOR, "button.ant-btn-primary").click()
    print("   ✅ 下一步已點擊")
    time.sleep(2)

    # ── Step 4: 輸入密碼 ──────────────────────────────────────────────────────
    print("📍 Step 4: 輸入密碼")
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))
    )
    password_input.clear()
    password_input.send_keys(_PASSWORD)
    password_input.send_keys(Keys.RETURN)
    print("   ✅ 密碼已送出")
    time.sleep(3)

    # ── Step 5: 驗證登入成功 ──────────────────────────────────────────────────
    print("📍 Step 5: 驗證登入成功")
    agent_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(), 'Agent')]"))
    )
    assert len(agent_elements) > 0, "登入失敗：未找到 Agent 相關元素"
    print(f"   ✅ 登入成功！URL: {driver.current_url}")
