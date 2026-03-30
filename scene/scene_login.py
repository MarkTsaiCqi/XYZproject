from page.login import LoginPage


class LoginScene:
    def __init__(self, driver):
        self.login = LoginPage(driver)
        self.driver = driver

    def login_scene(self, email, password):
        """執行完整登入流程，回傳登入狀態字串"""
        self.login.open_login_modal()
        self.login.input_email(email)
        self.login.click_email_next()
        self.login.input_password(password)
        self.login.click_login()
        return self.login.check_login_user()






