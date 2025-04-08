import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NavigationPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button_selector = "svg[aria-hidden='true'][width='32'][height='32']"
    
    def is_menu_button_visible(self):
        """检查菜单按钮是否可见"""
        menu_buttons = self.driver.find_elements(By.CSS_SELECTOR, self.menu_button_selector)
        return len(menu_buttons) > 0
    
    def get_window_width(self):
        """获取当前窗口宽度"""
        return self.driver.get_window_size()['width']
    
    def resize_window(self, width, height=None):
        """调整窗口大小"""
        if height is None:
            height = self.driver.get_window_size()['height']
        self.driver.set_window_size(width, height)
    
    def click_menu_button(self):
        """点击菜单按钮"""
        menu_button = self.driver.find_element(By.CSS_SELECTOR, self.menu_button_selector)
        menu_button.click() 