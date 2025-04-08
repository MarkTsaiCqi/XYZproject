import allure
import pytest
from scene.scene_login import LoginScene
from XYZ_tuil import GetDriver


# 设置该方法是获取网页driver驱动对象。
@pytest.fixture(autouse=True)
def getdriver():
    driver = GetDriver().get_web_driver()
    return driver


class TestWEBLogin:
    # 执行登陆的case
    def test_login(self, getdriver):
        # 获取驱动
        driver = getdriver
        try:
            # 传输驱动到LoginScene方法
            loginuser = LoginScene(driver).login_scene("admin", "runde123456")
            print(loginuser)
            assert loginuser == "超级管理员"
        except Exception as e:
            # log2.info("执行登陆的case失败，失败原因:{}".format(e))
            raise e


    def test_object(self):
        assert 1==1
        print("22222222222222222222222")

    def test_test01(self):
        a ="12"
        b ="123465"
        print("3333333333333333333333333")
        assert (a in b)

    def test_test02(self):
        a,b = 1,2
        print("44444444444444444444")
        assert (a == b)








