from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

def test_xyz_login_email():
    """测试 Email 登录功能"""
    selenium_url = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless=new")

    driver = webdriver.Remote(command_executor=selenium_url, options=options)

    # 登录凭据
    email = "xyzdev01@cqigames.com"
    password = "Abc123123?"

    try:
        print("🚀 开始登录测试...")
        
        # 步骤 1: 打开首页
        print("📍 步骤 1: 打开首页")
        driver.get("https://xyz-beta.protago-dev.com/home")
        time.sleep(3)
        print(f"📍 Current URL: {driver.current_url}")
        print(f"📍 Title: {driver.title}")

        # 步骤 2: 点击 Login 按钮
        print("📍 步骤 2: 点击 Login 按钮")
        login_selectors = [
            (By.XPATH, "//*[normalize-space(text())='Sign Up / Log In']"),
            (By.XPATH, "//*[contains(text(), 'Sign Up / Log In')]"),
            (By.XPATH, "//*[contains(text(), 'Log In')]"),
        ]
        
        login_found = False
        for by_type, selector in login_selectors:
            try:
                login_link = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((by_type, selector))
                )
                if login_link.is_displayed():
                    login_link.click()
                    print("✅ 已点击 Login 按钮")
                    login_found = True
                    break
            except:
                continue
        
        if not login_found:
            raise Exception("找不到 Login 按钮")
        
        time.sleep(2)

        # 步骤 3: 输入 Email
        print("📍 步骤 3: 输入 Email")
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='example@site.com']"))
        )
        email_input.clear()
        email_input.send_keys(email)
        print(f"✅ Email 已输入: {email}")
        time.sleep(1)

        # 步骤 4: 点击下一步按钮
        print("📍 步骤 4: 点击下一步按钮")
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ant-btn-primary .anticon-arrow-right"))
            )
            next_button.click()
        except:
            # 备用方案：点击父按钮
            parent_button = driver.find_element(By.CSS_SELECTOR, "button.ant-btn-primary")
            parent_button.click()
        print("✅ 已点击下一步按钮")
        time.sleep(2)

        # 步骤 5: 输入密码
        print("📍 步骤 5: 输入密码")
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))
        )
        password_input.clear()
        password_input.send_keys(password)
        print("✅ 密码已输入")
        time.sleep(1)

        # 步骤 6: 按 Enter 键登录
        print("📍 步骤 6: 按 Enter 键登录")
        password_input.send_keys(Keys.RETURN)
        print("✅ 已按下 Enter 键，正在登录...")
        time.sleep(3)

        # 步骤 7: 验证登录成功
        print("📍 步骤 7: 验证登录成功")
        current_url_after_login = driver.current_url
        print(f"📍 登录后 URL: {current_url_after_login}")
        
        # 检查是否出现 Agent 相关元素（登录成功的指示器）
        agent_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(), 'Agent')]"))
        )
        
        assert len(agent_elements) > 0, "登录失败：未找到 Agent 相关元素"
        print("✅ 登录成功！检测到 Agent 相关元素")
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        driver.save_screenshot("login_test_error.png")
        raise
    finally:
        driver.quit()
