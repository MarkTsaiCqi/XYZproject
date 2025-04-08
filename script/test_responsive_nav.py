import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
import time
from page.navigation_page import NavigationPage

def test_responsive_navigation():
    # 初始化浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # 初始化页面对象
        nav_page = NavigationPage(driver)
        
        # 访问测试页面
        driver.get("https://xyz-beta.protago-dev.com/home")
        
        # 等待页面加载
        time.sleep(2)
        
        # 获取初始窗口大小
        initial_width = nav_page.get_window_width()
        
        # 检查初始状态下是否存在菜单按钮
        assert not nav_page.is_menu_button_visible(), "初始状态下不应该显示菜单按钮"
        
        # 逐步缩小窗口宽度
        for width in range(initial_width, 800, -50):
            nav_page.resize_window(width)
            time.sleep(0.5)
            
            # 检查是否出现菜单按钮
            if nav_page.is_menu_button_visible():
                print(f"在窗口宽度 {width}px 时检测到菜单按钮")
                break
        
        # 验证菜单按钮是否出现
        assert nav_page.is_menu_button_visible(), "窗口缩小后应该显示菜单按钮"
        
        # 点击菜单按钮
        nav_page.click_menu_button()
        time.sleep(1)
        
        # 验证菜单是否展开
        # 这里需要根据实际页面结构添加相应的验证逻辑
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_responsive_navigation() 