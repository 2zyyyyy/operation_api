# @File:test_getusermenu.py
# @Author:2zyyyyy
# @Time:2019年05月16日
# @Explain: 获取用户菜单
import json
import sys
from os import path
import allure
import pytest

from Params.params import GetUserMenu
from Config.Config import Config
from Common import Request
from Common import Consts
from Common import Assert

sys.path.append(path.dirname(path.abspath(__file__)))


class TestGetUserMenu:
    @allure.feature('GetUserMenu')
    @allure.severity('blocker')
    @allure.story('GetUserMenu')
    def test_getusermenu_01(self, action):
        """
            用例描述：systemId、terminalType正常
        """
        conf = Config()
        data = GetUserMenu()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_base
        req_url = 'http://' + host
        urls = data.url
        params = data.data
        headers = data.header

        he = {'Content-Type': 'application/json;charset=UTF-8', 'token': "fbe62213-d9f6-4805-b239-1c232c5f2a9f"}

        api_url = req_url + urls[0]
        response = request.post_request(api_url, json.dumps(he), headers[0])

        print(json.dumps(he))
        assert test.assert_code(response['body']['code'], '1003')
        # assert test.assert_body(response['body'], 'description', '密码错误')
        # assert test.assert_time(response['time_consuming'], 200)
        Consts.RESULT_LIST.append('True')
