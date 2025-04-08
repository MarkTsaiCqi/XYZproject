import time
from selenium.webdriver.common.by import By
from base.base import BaseAction
import page

"""
    封装”用户管理“页面的可操作元素
"""
# 用户管理，新增按钮
UG_ADD_BUTTON = By.XPATH, "//*[@id='das']/div/div[1]/button"

# -------用户管理新增界面---------
# 用户名称
UG_USER_NAME = By.XPATH, "//*[@id='das']/div/div[3]/div/div[2]/div/form/div[1]/div[1]/div/div/div/input"
# 登录名
UG_LOGIN_NAME = By.XPATH, "//*[@id='das']/div/div[3]/div/div[2]/div/form/div[1]/div[2]/div/div/div/input"
# 登录密码
UG_LOGIN_PASSWORD = By.XPATH, "//*[@id='das']/div/div[3]/div/div[2]/div/form/div[2]/div[1]/div/div/div/input"
# 手机号码
UG_PHONE = By.XPATH, "//*[@id='das']/div/div[3]/div/div[2]/div/form/div[2]/div[2]/div/div/div/input"
# 备注
UG_CONTENT = By.XPATH, "//*[@id='das']/div/div[3]/div/div[2]/div/form/div[3]/div[1]/div/div/div/input"
# 角色类型
UG_ROLE_TYPE = By.XPATH, "//*[@id='das']/div/div[3]/div/div[2]/div/form/div[3]/div[2]/div/div/div/div[1]/input"
# 角色类型数据
UG_ROLE_TYPE_DATE = By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li"
# 数据权限
UG_DATE_POWER = By.XPATH, "//*[@id='das']/div/div[3]/div/div[2]/div/form/div[4]/div[1]/div/div/div/input"
# 是否启用
UG_ENABLE = By.XPATH, "//*[@id='das']/div/div[3]/div/div[2]/div/form/div[1]/div[1]/div/div/div/input"
# 确定按钮
UG_DEFINE_BUTTON = By.XPATH, "//*[@id='das']/div/div[3]/div/div[3]/span/button[1]"
# 取消按钮
UG_CANCEL_BUTTON = By.XPATH, "//*[@id='das']/div/div[3]/div/div[3]/span/button[2]"


class UserPage:
    def __init__(self, driver):
        self.driver = BaseAction(driver)

    def click_add(self):
        self.driver.base_click(UG_ADD_BUTTON)

    def input_user_name(self, value):
        self.driver.base_input(UG_USER_NAME, value)

    def input_login_name(self, value):
        self.driver.base_input(UG_LOGIN_NAME, value)

    def input_login_password(self, value):
        self.driver.base_input(UG_LOGIN_PASSWORD, value)

    def input_phone(self, value):
        self.driver.base_input(UG_PHONE, value)

    def input_content(self, value):
        self.driver.base_input(UG_CONTENT, value)

    def click_role_type(self):
        self.driver.base_click(UG_ROLE_TYPE)
        time.sleep(0.5)
        self.driver.base_click(UG_ROLE_TYPE_DATE, -2)

    def click_date_power(self):
        self.driver.base_scroll_element(UG_DATE_POWER)
        self.driver.base_click(UG_DATE_POWER)

    def click_define(self):
        self.driver.base_click(UG_DEFINE_BUTTON)

    def click_cancel(self):
        self.driver.base_click(UG_CANCEL_BUTTON)



"""
    封装”角色管理“页面的可操作元素
"""
# 角色管理，新增按钮
JE_ADD_BUTTON = By.XPATH, "//*[@id='das']/div/div[1]/button"

# -------角色管理新增界面---------
# 角色名称
JS_ROLE_NAME = By.XPATH, "//*[@id='das']/div/div[3]/div/div[2]/div/form/div[1]/div[1]/div/div/div/input"
# 备注
JS_CONTENT = By.XPATH, "//*[@id='das']/div/div[3]/div/div[2]/div/form/div[1]/div[2]/div/div/div/input"
# 使用模板
JS_TEMPLATE = By.XPATH, "//*[@id='das']/div/div[3]/div/div[2]/div/form/div[2]/div/div/div/div/div/input"
# 模板列表元素
JS_TEMPLATE_DATE = By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li"
# 确定按钮元素
JS_DEFINE_BUTTON = By.XPATH, "//*[@id='das']/div/div[3]/div/div[3]/span/button[1]"
# 取消按钮元素
JS_CANCEL_BUTTON = By.XPATH, "//*[@id='das']/div/div[3]/div/div[3]/span/button[2]"


class RolePage:
    def __init__(self, driver):
        self.driver = BaseAction(driver)

    def click_add(self):
        self.driver.base_click(JE_ADD_BUTTON)

    def input_role_name(self, value):
        self.driver.base_input(JS_ROLE_NAME, value)

    def input_content(self, value):
        self.driver.base_input(JS_CONTENT, value)

    def click_template(self):
        self.driver.base_click(JS_TEMPLATE)
        time.sleep(0.3)
        self.driver.base_click(JS_TEMPLATE_DATE, -2)

    def click_define(self):
        self.driver.base_click(JS_DEFINE_BUTTON)

    def click_cancel(self):
        self.driver.base_click(JS_CANCEL_BUTTON)




