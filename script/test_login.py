import sys
import os
import time  # 引入 time 模組
# 將專案根目錄加入 Python 路徑
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from page.login import LoginPage
from XYZ_tuil import GetDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def getdriver():
    driver = GetDriver().get_web_driver()
    yield driver
    driver.quit()

class TestLogin:
    def test_email_login(self, getdriver):
        driver = getdriver
        login_page = LoginPage(driver)

        # 執行登入流程
        login_page.login_with_email(
            email="xyzdev01@cqigames.com",
            password="Abc123123?"
        )

        # 等待五秒鐘
        time.sleep(5)

        # 點擊 "Agent" 按鈕
        agent_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'navItem cursor-pointer text-[16px] h-[80px] activeNav')]"))
        )
        agent_button.click()

        # 跳轉到設定頁面
        driver.get("https://xyz-beta.protago-dev.com/Setting")

        # 等待 E-mail 欄位出現
        email_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div[2]"))
        )

        # 判斷 E-mail 欄位是否存在
        assert email_element is not None, "E-mail 欄位元素未出現"
        assert email_element.text == "xyzdev01@cqigames.com", "E-mail 欄位中的值不正確"
