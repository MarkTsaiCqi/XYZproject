from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

def test_xyz_login_email():
    """测试 Email 登录功能"""
    selenium_url = os.getenv("SELENIUM_REMOTE_URL")
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless=new")

    # 如果设置了 SELENIUM_REMOTE_URL，使用 Selenium Grid
    # 否则使用本地浏览器
    if selenium_url:
        print(f"🌐 使用 Selenium Grid: {selenium_url}")
        driver = webdriver.Remote(command_executor=selenium_url, options=options)
    else:
        print("💻 使用本地 Chrome 浏览器")
        try:
            driver = webdriver.Chrome(options=options)
        except Exception as e:
            print(f"❌ 无法创建本地浏览器: {e}")
            print("💡 请设置 SELENIUM_REMOTE_URL 环境变量，或确保已安装 ChromeDriver")
            raise

    # 登录凭据
    email = "xyzdev01@cqigames.com"
    password = "Abc123123?"

    try:
        print("🚀 开始登录测试...")
        
        # 步骤 0: 清除 cookies 和缓存（确保未登录状态）
        print("📍 步骤 0: 清除 cookies 和缓存")
        driver.delete_all_cookies()
        print("✅ 已清除 cookies")
        
        # 步骤 1: 打开首页
        print("📍 步骤 1: 打开首页")
        driver.get("https://xyz-beta.protago-dev.com/home")
        
        # 等待页面完全加载
        WebDriverWait(driver, 15).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        time.sleep(2)  # 额外等待，确保动态内容加载
        
        print(f"📍 Current URL: {driver.current_url}")
        print(f"📍 Title: {driver.title}")
        
        # 检查页面是否已登录
        print("🔍 检查页面登录状态...")
        try:
            agent_elements = driver.find_elements(By.XPATH, "//span[contains(text(), 'Agent')]")
            if agent_elements and len(agent_elements) > 0:
                print("⚠️  检测到页面可能已登录（找到 Agent 相关元素）")
                print("💡 尝试清除 localStorage 和 sessionStorage...")
                try:
                    driver.execute_script("window.localStorage.clear();")
                    driver.execute_script("window.sessionStorage.clear();")
                    print("✅ 已清除 localStorage 和 sessionStorage")
                    
                    # 清除 cookies 后重新导航到首页
                    driver.delete_all_cookies()
                    driver.get("https://xyz-beta.protago-dev.com/home")
                    WebDriverWait(driver, 15).until(
                        lambda d: d.execute_script("return document.readyState") == "complete"
                    )
                    time.sleep(3)
                    print(f"📍 刷新后 URL: {driver.current_url}")
                except Exception as e:
                    print(f"⚠️  清除缓存失败: {e}")
        except:
            pass

        # 步骤 2: 检查是否需要登录
        print("📍 步骤 2: 检查登录状态")
        
        # 先检查是否已经登录
        already_logged_in = False
        try:
            agent_check = driver.find_elements(By.XPATH, "//span[contains(text(), 'Agent')]")
            if agent_check and len(agent_check) > 0:
                print("✅ 检测到页面已登录，跳过登录步骤")
                already_logged_in = True
        except:
            pass
        
        if not already_logged_in:
            # 步骤 2.1: 点击 Login 按钮
            print("📍 步骤 2.1: 点击 Login 按钮")
            login_selectors = [
                (By.XPATH, "//*[normalize-space(text())='Sign Up / Log In']"),
                (By.XPATH, "//*[contains(text(), 'Sign Up / Log In')]"),
                (By.XPATH, "//*[contains(text(), 'Log In')]"),
                (By.XPATH, "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'log in')]"),
                (By.XPATH, "//button[contains(text(), 'Log In')]"),
                (By.XPATH, "//a[contains(text(), 'Log In')]"),
            ]
            
            login_found = False
            for by_type, selector in login_selectors:
                try:
                    print(f"   🔍 尝试定位: {selector[:50]}...")
                    login_link = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((by_type, selector))
                    )
                    if login_link.is_displayed():
                        print(f"   ✅ 找到可见的 Login 按钮")
                        login_link.click()
                        print("✅ 已点击 Login 按钮")
                        login_found = True
                        break
                    else:
                        print(f"   ⚠️  找到元素但不可见")
                except Exception as e:
                    print(f"   ❌ 未找到: {str(e)[:50]}")
                    continue
            
            if not login_found:
                # 保存调试截图
                driver.save_screenshot("login_button_not_found.png")
                print("📸 调试截图已保存: login_button_not_found.png")
                
                # 尝试查找所有包含 "log" 的元素
                try:
                    print("🔍 查找所有包含 'log' 的元素...")
                    all_elements = driver.find_elements(By.XPATH, "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'log')]")
                    print(f"📊 找到 {len(all_elements)} 个相关元素:")
                    for i, elem in enumerate(all_elements[:10]):  # 只显示前10个
                        try:
                            print(f"   {i+1}. 文本='{elem.text[:50]}', 标签={elem.tag_name}, 可见={elem.is_displayed()}")
                        except:
                            pass
                except:
                    pass
                
                raise Exception("找不到 Login 按钮")
            
            time.sleep(2)

        # 步骤 3: 输入 Email（如果未登录）
        if not already_logged_in:
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
