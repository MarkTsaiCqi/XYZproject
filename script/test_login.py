import sys
import os
# 將專案根目錄加入 Python 路徑
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from page.login import LoginPage
from XYZ_tuil import GetDriver

@pytest.fixture(autouse=True)
def getdriver():
    driver = GetDriver().get_web_driver()
    yield driver
    driver.quit()

class TestLogin:
    def test_email_login(self, getdriver):
        driver = getdriver
        try:
            # 建立 LoginPage 實例
            login_page = LoginPage(driver)
            
            # 執行登入流程
            login_page.login_with_email(
                email="xyzdev01@cqigames.com",
                password="Abc123123?"
            )
            
            # TODO: 加入登入成功的驗證
            # 例如：檢查是否有登入成功的元素出現
            
        except Exception as e:
            # 如果需要，可以在這裡加入簡單的錯誤處理
            raise e
