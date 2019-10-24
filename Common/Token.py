# @File:Token.py
# @Author:2zyyyyy
# @Time:2019年03月13日
# @Explain: 封装获取token方法

import requests
from Common import Log
from Config import Config


class Token:
    def __init__(self):
        self.log = Log.MyLog()
        self.config = Config.Config()

    def get_token(self, env):
        """
        获取token
        :param env: 环境变量
        :return:
        """
        headers = {
            'Content-Type': 'application/json;charset=UTF-8'
        }

        if env == 'base':
            login_url = 'http://' + self.config.host_base + self.config.loginHost_base
            parm = self.config.loginInfo_base
            # print(login_url)

            response = requests.post(login_url, parm, headers=headers)
            result = response.json()
            token_base = result["result"]["token"]
            self.log.debug('token: %s' % token_base)
            print(result)
            return token_base

        elif env == 'pre':
            login_url = 'http://' + self.config.host_base + self.config.loginHost_pre
            parm = self.config.loginInfo_pre
            print(login_url)

            response = requests.post(login_url, data=parm, headers=headers)
            result = response.json()
            token_pre = result["result"]["token"]
            self.log.debug('token: %s' % token_pre)
            return token_pre

        elif env == 'pro':
            login_url = 'http://' + self.config.host_pro + self.config.loginHost_pro
            parm = self.config.loginInfo_pro
            print(login_url)

            response = requests.post(login_url, data=parm, headers=headers)
            result = response.json()
            token_pro = result["result"]["token"]
            self.log.debug('token: %s' % token_pro)
            return token_pro


if __name__ == '__main__':
    to = Token()
    to.get_token('base')
