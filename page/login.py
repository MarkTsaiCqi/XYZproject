from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base import BaseAction

"""
    封装登录页面的可操作元素
"""
# 定位器
LOGIN_LINK = By.XPATH, "//span[contains(text(), 'Log in')]"
LOGIN_EMAIL_INPUT = By.CSS_SELECTOR, "input[placeholder='example@site.com']"
LOGIN_PASSWORD_INPUT = By.CSS_SELECTOR, "input[placeholder='Password']"
# 新增：email 輸入後的箭頭按鈕
EMAIL_NEXT_BUTTON = By.CSS_SELECTOR, "button.ant-btn-primary .anticon-arrow-right"

class LoginPage:
    def __init__(self, driver):
        self.driver = BaseAction(driver)

    def click_login_link(self):
        """點擊登入連結"""
        self.driver.base_click(LOGIN_LINK)

    def input_email(self, email):
        """輸入 Email"""
        self.driver.base_input(LOGIN_EMAIL_INPUT, email)

    def click_email_next(self):
        """點擊 email 輸入後的箭頭按鈕"""
        self.driver.base_click(EMAIL_NEXT_BUTTON)

    def input_password(self, password):
        """輸入密碼"""
        self.driver.base_input(LOGIN_PASSWORD_INPUT, password)

    def submit_login_with_enter(self):
        """在密碼欄位按下 Enter 鍵"""
        self.driver.base_input(LOGIN_PASSWORD_INPUT, Keys.RETURN)

    def login_with_email(self, email, password):
        """執行 Email 登入流程"""
        self.click_login_link()
        self.input_email(email)
        self.click_email_next()  # 新增：點擊箭頭按鈕
        self.input_password(password)
        self.submit_login_with_enter()
