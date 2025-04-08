import os
import unittest
import pytest
from config import DIR_PATH

# unittest:执行方法
# suite = unittest.defaultTestLoader.discover("./script")
# file_path = DIR_PATH + os.sep + "report" + os.sep + "tpshop_auto.html"
# HTMLTestReport(file_path).run(suite)

# pytest：执行方法
if __name__ == "__main__":
    # 判断tmp有没有旧数据，有循环删除，清理旧tmp里的allure报告的数据
    try:
        file_list = os.listdir('./report_pytest/tmp')
        if int(len(file_list)) >= 1:
            for filename in file_list:
                os.remove("./report_pytest/tmp/" + filename)  # 删除一个文件
    except Exception as e:
        print(e)
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['--alluredir=./report_pytest/tmp','-s'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告，同时clean旧数据
    os.system('allure generate ./report_pytest/tmp -o ./report_pytest/html --clean')

