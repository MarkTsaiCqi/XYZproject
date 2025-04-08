from selenium.webdriver.common.by import By
from base.base import BaseAction

"""
    封装登录页面的可操作元素
"""
LOGIN_BUTTON = By.XPATH, "//*[@id='root']/div/div/div/div[1]/div/div/div[2]/div/span"
LOGIN_USERNAME = By.XPATH, "/html/body/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[3]/div[1]/div/span/input"
LOGIN_USERNAME_NEXT = By.XPATH, "/html/body/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[3]/div[1]/div/span/" \
                                "span[2]/button"
LOGIN_PASSWORD = By.XPATH, "/html/body/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/span/input"
LOGIN_BUTTON_CONFIRM = By.XPATH, "/html/body/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[5]/button"
CHECK_LOGIN_USERNAME = By.XPATH, "//*[@id='root']/div/div/div/div[1]/div[1]/div/div[2]/div/div/span[1]"


class LoginPage:
    def __init__(self, driver):
        self.driver = BaseAction(driver)

    # 获取点击弹出登录密码框
    def input_login_button(self):
        self.driver.base_click(LOGIN_BUTTON)

    # 输入账号
    def input_account(self, value):
        self.driver.base_input(LOGIN_USERNAME, value)

    # 点击下一步
    def input_user_next(self):
        self.driver.base_click(LOGIN_USERNAME_NEXT)

    # 输入密码
    def input_password(self, value):
        self.driver.base_input(LOGIN_PASSWORD, value)

    # 点击登录
    def click_login(self):
        self.driver.base_click(LOGIN_BUTTON_CONFIRM)

    # 获取登录的用户名
    def check_login_user(self):
        return self.driver.base_text(CHECK_LOGIN_USERNAME)

    # 滚动条操作
    def pull_scroll(self, value):
        self.driver.base_scroll_element(value)
