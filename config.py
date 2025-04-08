"""
    项目的所有配置文件信息
    app：账号：13436418388 密码：123456
    web后台:账号：admin 密码：123456
"""

# 要测试的网址
import os.path

# webosocket连接地址：
WEBSOCKETURL = ''

# 项目RUL地址：
# XYZ测试地址：https://xyz-beta.protago-dev.com/
# XYZ开发地址：https://xyz.netmind.ai/
# XYZ测试地址：
URL = "https://xyz-beta.protago-dev.com/"



# 当前项目路径
DIR_PATH = os.path.dirname(__file__)
# 获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 测试连接的手机版本和设备地址/设备号
PHONE_VERSION = '6.0.1'
# mumu模拟器连接地址
DEVICE_NAME = "127.0.0.1:755"
# 要测试的Android包名，和界面名
APP_PACK = "com.tpshop.malls"
APP_ACTIVITY = ".SPMainActivity"



