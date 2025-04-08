import time
from time import sleep
from base.base import BaseAction
from XYZ_tuil import GetDriver
from page.system_set import RolePage,UserPage
from page.menu_manage import MenuManage
from scene.scene_login import LoginScene


class SystemSetScene:
    def __init__(self, driver):
        self.menu = MenuManage(driver)
        self.role = RolePage(driver)
        self.user = UserPage(driver)


    # 新增用户场景
    def add_user(self, name, loginname, password, phone, content):
        # self.menu.menu_system_set()
        # self.menu.menu_user_manage()
        self.user.click_add()
        self.user.input_user_name(name)
        self.user.input_login_name(loginname)
        self.user.input_login_password(password)
        self.user.input_phone(phone)
        self.user.input_content(content)
        self.user.click_role_type()
        time.sleep(0.5)
        self.user.click_define()

    # 新增角色场景
    def add_role(self, name, content):

        self.role.click_add()
        self.role.input_role_name(name)
        self.role.input_content(content)
        self.role.click_template()
        time.sleep(0.2)
        # self.role.click_cancel()
        self.role.click_define()

    def add_message(self):
        pass

if __name__ == '__main__':
    driver = GetDriver.get_web_driver()
    loginuser = LoginScene(driver).login_scene("admin", "runde123456")
    a = SystemSetScene(driver)
    a.add_user("用户名", "login", "123456", "1382736442", "备注啊")

