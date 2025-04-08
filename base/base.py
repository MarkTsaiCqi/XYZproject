from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support.select import Select
from base import DirAndTime
from base import log
"""
    封装selenium的基础操作方法
"""


class BaseAction:
    def __init__(self, driver):
        log.info("正在初始化，driver对象：{}".format(driver))
        self.driver = driver

    # 查找元素定位
    def find_element(self, loc):
        try:
            log.info("正在查找定位元素位置：{}".format(loc))
            element = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(
                    lambda x: x.find_element(*loc))
            return element
        except Exception as e:
            log.info("查找元素定位失败：{}".format(loc))
            log.info("-------定位元素失败，抛出的错误数据-------：{}".format(e))
            raise e

    # 查找多元素定位
    def find_elements(self, loc, *args):
        try:
            log.info("正在查找定位元素位置：{}".format(loc))
            element = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(
                lambda x: x.find_elements(*loc))
            return element
        except Exception as e:
            log.info("查找元素定位失败：{}".format(loc))
            raise e

    # 刷新当前页面方法
    def refresh_page(self):
        self.driver.refresh()
        time.sleep(1)

    # 调用截图方法
    def screenshot(self):
        try:
            imagepath = DirAndTime.createCurrentDateDir() + "\\"
            self.driver.get_screenshot_as_file(imagepath + "error_{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
        except Exception as e:
            log.info("执行截图方法失败，失败详情日志：{}".format(e))


    # 鼠标移动到指定位置方法
    def mouce_move(self, loc):
        log.info("正在初始化执行鼠标移动方法：{}".format(loc))
        element = self.find_element(loc)
        ActionChains(self.driver).move_to_element(element).perform()

    # 执行点击方法
    def base_click(self, loc, *args):
        log.info("正在初始化执行点击方法：{}".format(loc))
        if len(args) > 0:
            data = int(args[0])
            element = (self.find_elements(loc))[data]
        else:
            element = self.find_element(loc)
        element.click()

    # 执行输入方法
    def base_input(self, loc, value, *args):
        log.info("正在初始化执行输入方法：{}".format(loc))
        if len(args) > 0:
            data = int(args[0])
            element = self.find_element(loc)[data]
        else:
            element = self.find_element(loc)
        element.clear()
        element.send_keys(value)
        return element

    # 固定像素滚动方法
    def base_scroll(self, xpx=0, ypx=0):
        log.info("正在初始化执行页面滚动方法")
        self.driver.execute_script('window.scrollBy(0,{})'.format(ypx))

    # 滚动页面至元素可见
    def base_scroll_element(self, loc):
        log.info("正在初始化执行滚动方法：{}".format(loc))
        element = self.find_element(loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # 执行上传文件方法,只支持input标签上传
    def base_file_input(self, loc, path):
        log.info("正在初始化执行上传文件方法：{}".format(loc))
        element = self.find_element(loc)
        element.send_keys(path)

    # 执行获取span文本
    def base_span(self, loc, *args):
        if len(args) > 0:
            data = int(args[0])
            element = self.find_element(loc)[data]
        else:
            element = self.find_element(loc)
        span = element.get_attribute('innerHTML')
        return span

    # 执行获取文本
    def base_text(self, loc, *args):
        if len(args) > 0:
            data = int(args[0])
            element = self.find_element(loc)[data]
        else:
            element = self.find_element(loc)
        return element.text
    
    # 该包只适用于HTML+option原生下拉框,下拉框选择
    def base_select(self, loc):
        element = self.find_element(loc)
        select = Select(element)
        # select.select_by_index(index)
        # select.select_by_value(value)
        # select.select_by_visible_text(text)

    # 执行获取元素属性值:id,name,text....
    def base_attribute(self, loc, value):
        element = self.find_element(loc)
        return element.get_attribute(value)

    # 执行判断元素是否可见:True or False
    def base_displayed(self, loc):
        element = self.find_element(loc)
        return element.is_displayed()

    # 执行判断元素是否选中:True or False
    def base_selected(self, loc):
        element = self.find_element(loc)
        return element.is_selected()

    # 检查frame是否存在，存在则切换进frame中
    def frame(self,loc):
        element = self.find_element(loc)

    # app两点之间的滑动方法
    def base_swipe(self):
        self.driver.swipe(400, 1200, 400, 500, duration=1000)

    # app两点之间的平滑滑动方法（不会有惯性）
    def base_swipe_slow(self):
        TouchAction(self.driver).press(x=200,y=1100).wait(100).move_to(x=200, y=200).release().perform()








