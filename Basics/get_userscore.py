# @File:get_userscore.py
# @Author:2zyyyyy
# @Time:2019年03月13日
# @Explain: 获取用户菜单列表
import json
import pprint

import requests

from Basics import get_token


def get_score():
    url = 'http://192.168.0.202:8071/dataScope-service/getDataScopeByToken'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'token': get_token.login()
    }
    payload = {
        "userMobile": "18067940805",
        "userName": "西西沃",
        "systemId": "222",
        "terminalType": "78",
        "password": "123456"
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    results = response.json()
    return results


if __name__ == '__main__':
    print(get_token.login())
    pprint.pprint(get_score())
