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

    # 定義元素定位器
    CREATE_AGENT_BUTTON = By.XPATH, "//span[contains(text(), 'Create Agent')]"
    AGENT_TYPE_RADIO = By.XPATH, "//input[@name=':r8:'][@value='1']"  # 預設的 Agent Type
    NEXT_BUTTON = By.XPATH, "//button[contains(span/text(), 'Next')]"
    UPLOAD_AVATAR_BUTTON = By.XPATH, "//span[contains(text(), 'Upload avatar')]"
    AVATAR_INPUT = By.CSS_SELECTOR, "input[type='file']"  # 假設的檔案上傳 input
    OK_BUTTON = By.XPATH, "//button[contains(span/text(), 'OK')]"
    NAME_INPUT = By.ID, "name"
    AGENT_IDENTITY_TYPE = By.XPATH, "//div[contains(text(), 'Private Agent')]"
    
    # 更新 E-mail 行的定位器
    EMAIL_ROW = By.XPATH, "//div[contains(@class, 'row-between p-20')]//span"

    def create_agent(self, name, avatar_path, email, token):
        """創建 agent 的流程"""
        # 點擊 Create Agent 按鈕
        self.driver.base_click(self.CREATE_AGENT_BUTTON)

        # 選擇預設的 Agent Type
        self.driver.base_click(self.AGENT_TYPE_RADIO)

        # 點擊 Next 按鈕
        self.driver.base_click(self.NEXT_BUTTON)

        # 上傳 avatar
        self.driver.base_click(self.UPLOAD_AVATAR_BUTTON)
        self.driver.base_input(self.AVATAR_INPUT, avatar_path)  # 上傳檔案

        # 點擊 OK 按鈕
        self.driver.base_click(self.OK_BUTTON)

        # 輸入 Name
        self.driver.base_input(self.NAME_INPUT, name)

        # 選擇 Private Agent
        self.driver.base_click(self.AGENT_IDENTITY_TYPE)

        # 拍照（這裡可以根據需要加入截圖的邏輯）
        self.driver.screenshot()  # 假設 base.py 中有這個方法

    def get_email_row_text(self):
        """獲取 E-mail 行的文本"""
        email_row_element = self.driver.find_element(self.EMAIL_ROW)
        return email_row_element.text
