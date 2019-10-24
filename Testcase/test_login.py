# @File:test_login.py
# @Author:2zyyyyy
# @Time:2019年04月16日
# @Explain: 用户登录接口测试

import sys
from os import path
import allure
from Params.params import Login
from Config.Config import Config
from Common import Request
from Common import Consts
from Common import Assert

sys.path.append(path.dirname(path.abspath(__file__)))


class TestLogin:

    @allure.feature('Login')
    @allure.severity('blocker')
    @allure.story('Login')
    def test_login_01(self, action):
        """
            用例描述：账户密码正确 登录请求
        """
        conf = Config()
        data = Login()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_base
        req_url = 'http://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[0]
        response = request.post_request(api_url, params[0], headers[0])

        print(headers[0])
        assert test.assert_code(response['body']['code'], '1005')
        assert test.assert_body(response['body'], 'description', '密码错误')
        assert test.assert_time(response['time_consuming'], 200)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Login')
    @allure.severity('blocker')
    @allure.story('Login')
    def test_login_02(self, action):
        """
            用例描述：账户正确密码错误 登录失败
        """
        conf = Config()
        data = Login()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_base
        req_url = 'http://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[0]
        response = request.post_request(api_url, params[1], headers[0])

        assert test.assert_code(response['body']['code'], '1005')
        assert test.assert_body(response['body'], 'description', '密码错误')
        assert test.assert_time(response['time_consuming'], 200)
        Consts.RESULT_LIST.append('True')
