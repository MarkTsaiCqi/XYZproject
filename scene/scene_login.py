from time import sleep
from base.base import BaseAction
from XYZ_tuil import GetDriver
from page.login import LoginPage


class LoginScene:
    def __init__(self, driver):
        self.login = LoginPage(driver)
        self.driver = driver

    # 登陆
    def login_scene(self, username, password):
        self.login.input_login_button()
        self.login.input_account(username)
        self.login.input_user_next()
        self.login.input_password(password)
        sleep(0.5)
        self.login.click_login()
        # 调用截图方法。
        # BaseAction(self.driver).screenshot()
        sleep(2)
        longin_user = self.login.check_login_user()
        sleep(1)
        return longin_user


if __name__ == '__main__':
    driver = GetDriver.get_web_driver()
    s = LoginScene(driver)
    asd = s.login_scene("test1@qq.com", "123123aA")






