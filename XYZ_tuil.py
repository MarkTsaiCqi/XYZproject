import json
import time
from selenium import webdriver
try:
    from appium import webdriver as appdriver
except ModuleNotFoundError:
    appdriver = None
import config
import logging
import os
from logging.handlers import TimedRotatingFileHandler
from base.DirAndTime import getCurrentDate
from base.DirAndTime import getCurrentTime


class GetDriver:
    __app_driver = None
    __web_driver = None

    # 建立 Chrome 手機模擬 Driver（每次建立新 driver，不使用 singleton）
    @classmethod
    def create_mobile_web_driver(cls, device=None):
        if device is None:
            device = {
                "deviceMetrics": {"width": 393, "height": 851, "pixelRatio": 2.75, "touch": True},
                "userAgent": (
                    "Mozilla/5.0 (Linux; Android 11; Pixel 5) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/144.0.0.0 Mobile Safari/537.36"
                ),
            }
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", device)
        options.add_argument("--disable-notifications")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # 降低自動化特徵訊號，避免 Google 擋登入
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        selenium_url = os.getenv("SELENIUM_REMOTE_URL")
        if selenium_url:
            return webdriver.Remote(command_executor=selenium_url, options=options)
        return webdriver.Chrome(options=options)

    # 获取Web Driver
    @classmethod
    def get_web_driver(cls):
        if cls.__web_driver is None:
            cls.__web_driver = webdriver.Chrome()
            cls.__web_driver.get(config.URL)
            cls.__web_driver.maximize_window()
        return cls.__web_driver

    # 获取app Driver
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            # 设置启动
            desired_cpas = {}
            desired_cpas['platformName'] = 'Android'
            desired_cpas['platformVersion'] = config.PHONE_VERSION
            desired_cpas['devicesName'] = config.DEVICE_NAME
            desired_cpas['appPackage'] = config.APP_PACK
            desired_cpas['appActivity'] = config.APP_ACTIVITY
            # 默认输入中文无效，但不会报错，需要在 ”前置代码“ 中增加两个参数
            desired_cpas['unicodeKeyboard'] = True
            desired_cpas['resetKeyboard'] = True
            cls.__app_driver = appdriver.Remote('http://localhost:4723/wd/hub', desired_cpas)
        return cls.__app_driver


# 直接读取json文件工具
def read_json(filename, key):
    file_path = config.DIR_PATH + os.sep + "data" + os.sep + filename
    arrs = []
    with open(file_path, "r", encoding="utf-8")as f:
        for data in json.load(f).get(key):
            # 获取全部，
            arrs.append(tuple(data.values()))
            # 获取每一条的最后一个
            # arrs.append(tuple(data.values())[1:])
        return arrs

# 写如json文件工具
def write_json(value):
    file_path = config.DIR_PATH + os.sep + "data" + os.sep + "expect.json"
    with open(file_path,"w",encoding="utf-8")as f:
        data = {"expect":[{"desc":"app订单编号","order_no":value}]}
        json.dump(data,f)


# 日志封装
class GetLog:
    __log = None
    @classmethod
    def get_log(cls):
        if cls.__log is None:
            # 获取日志器对象
            cls.__log = logging.getLogger()
            # 设置入口级别
            cls.__log.setLevel(logging.DEBUG)
            # 获取处理器
            filename = config.DIR_PATH + os.sep + "log" + os.sep + getCurrentDate() + "_XYZ_auto.log"
            tf = logging.handlers.TimedRotatingFileHandler(filename=filename,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")

            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            tf.setFormatter(fm)
            # 将处理器添加到日志器
            cls.__log.addHandler(tf)
        # 返回日志器
        return cls.__log



if __name__ == '__main__':
    asd = read_json("R3_login.json","login")
    print(asd)
    print(asd[0][0])
    pass
