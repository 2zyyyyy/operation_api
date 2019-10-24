# @File:get_token.py
# @Author:2zyyyyy
# @Time:2019年03月13日
# @Explain: 获取200登录接口token值
import json

import requests


def login():
    url = 'http://192.168.0.202:8071/auth-service/login'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    payload = {
        "userMobile": "18067940805",
        "systemId": "111",
        "terminalType": "78",
        "password": "123456"
    }
    # response = requests.post(login_url, parm, headers=headers)
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    results = response.json()
    token = results["result"]["token"]
    return token


if __name__ == '__main__':
    res = login()
    print(res)
