# @Synopsis : 此文件是读取odps中的表字段，再调用某接口，返回生成的url连接
import json
import requests
import config
from script_url import login


# 调用接口，传入从表中读取到的两列
def get_message_manage(user, token):
    messageurl = config.URL+"api/system/app/feedback/detail/add"

    # 请求头根据自己接口文档进行调整
    headers = {'Content-Type': 'application/json', 'Authorization': token}
    data = {
        "msgType": 1,
        "msg": user+"的维保人员，自动化测试留言给平台数据"
    }
    data2 = {
        "feedbackId": 1595986791344185346,
        "msgType": 1,
        "msg": user+"的维保人员，自动化测试留言给平台数据"
    }

    #post方法
    r = requests.post(messageurl, json=data, headers=headers)
    asd = r.text
    print(asd)



if __name__ == '__main__':
    # token = login.interface_app_login("test14", "123456")
    token = '2c02d806-b5f7-407b-99a2-2e16f9925c9e'
    get_message_manage("asd", token)
