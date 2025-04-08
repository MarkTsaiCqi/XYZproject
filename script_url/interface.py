# -*- coding: utf-8 -*-
# @Time : 2021/12/6 9:59
# @Author : llh
# @File : test_api.py
# @Synopsis : 此文件是读取odps中的表字段，再调用某接口，返回生成的url连接
import re
import json
import requests
import pandas as pd



# 调用接口，传入从表中读取到的两列
def get_api():
    url = 'https://tlw-test.runde.pro/api/system/app/user/loginByAccount'
    login = "/api/system/app/user/loginByAccount"
    releas = "/api/system/app/feedback/detail/add"

    #请求头根据自己接口文档进行调整
    headers = {'Content-Type': 'application/json'}
    # headers = {'Content-Type': 'multipart/form-data'}
    s = {
        "account" : "zhong",
        "password" : "123456"
    }
    # s = json.dumps({
    #     "account" : "zhong",
    #     "password" : "123456"
    # })
    #post方法
    r = requests.get(url, params=s, headers=headers)
    resp_obj = json.loads(r.text)
    print(resp_obj)
    print(type(resp_obj))
    print(resp_obj["data"]["token"]["token"])
    #只获取到返回的json串中的data中的url值
    # data_list = resp_obj["data"]["Url"]
    # print(data_list)
    # return [id, data_list]


if __name__ == '__main__':
    get_api()
