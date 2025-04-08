import unittest
from time import sleep
from scene.scene_login import LoginScene
from XYZ_tuil import GetDriver


class TestCase(unittest.TestCase):
    # 初始化driver变量
    driver = None
    # 执行这个测试类，最开始只执行一次的方法

    @classmethod
    def setUpClass(cls) -> None:
        # 获取web的驱动
        cls.driver = GetDriver.get_web_driver()
        # 登陆场景调用
        scenelogin = LoginScene(cls.driver)
        scenelogin.login_scene("admin", "runde123456")
        sleep(3)

    # 每执行一个case前都会先执行这个函数
    def setUp(self) -> None: pass

    # 每执行一个case后都会先执行这个函数
    def tearDown(self) -> None: pass

    def test_newuser(self):
        sceneplatform = PlatformScene(self.driver)
        sceneplatform.newuser(2)
        # 循环创建用户，number个数
        sceneplatform.loopnewuser(10)


    # # demo使用
    # def test_demo(self):
    #     a,b =2, 2
    #     A = "AS"
    #     B = [1,2,3]
    #     print("这33333333333333333333")
    #     # 核实是否相等
    #     self.assertEqual(a, b)
    #     self.assertNotEqual(a, b)
    #     # 核实是否为真
    #     self.assertTrue(a)
    #     # 核实A是否在数列B中
    #     self.assertIn(A, B)

    # 执行这个测试类，最后只执行一次的方法
    @classmethod
    def tearDownClass(cls) -> None: pass


if __name__ == '__main__':
    unittest.main()
