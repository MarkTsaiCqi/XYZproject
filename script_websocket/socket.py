import time
import config
from websocket import create_connection
import websocket



class Test_websoket():

    def test_websk(self):
        # 登陆socket的账号数据
        logindata = "{act: 'ma_login',user_name: 'admin',pwd: '14946a0fbc4782e964b0b170fc505edc'," \
               "udid: 'aae681ab-42ed-5445-8d44-94c137d1e15d',passwd: 'admin123456'}"

        url = config.WEBSOCKETURL  # websocket连接地址
        websocket.enableTrace(True)  # 打开跟踪，查看日志
        ws = create_connection(url)  # 创建连接
        # ws.settimeout(10)   #设置超时时间
        # print(ws.gettimeout())  #获取超时时间
        print("获取连接状态：", ws.getstatus())
        print("获取请求头", ws.getheaders())
        # 发送登陆请求参数
        ws.send(logindata)
        # 获取请求后的返回值
        result = ws.recv()
        print("接收结果：", result)
        # 睡眠一段时间
        time.sleep(10)
        ws.send("{act:'3',i:'866652020996386'}")
        result = ws.recv()
        print("接收结果：", result)
        # 关闭长连接
        ws.close()

if __name__ == '__main__':
    asd = Test_websoket()
    asd.test_websk()