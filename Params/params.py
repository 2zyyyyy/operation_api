# @File:params.py
# @Author:2zyyyyy
# @Time:2019年04月15日
# @Explain: 定义所有测试数据

import os
from Params import tools
from Common import Log
from Common import Token

log = Log.MyLog()
path_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
print(path_dir)


def get_parameter(name):
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param


class Login:
    log.info('解析yaml，Path:' + path_dir + '/Params/Yaml/login.yaml')
    params = get_parameter('Login')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class GetUserMenu:
    log.info('解析yaml，Path:' + path_dir + '/Params/Yaml/getUserMenu.yaml')
    params = get_parameter('GetUserMenu')
    url = []
    data = []
    header = []
    # token = Token.Token()
    # get_token = token.get_token('base')
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])

    # header[0].append(get_token)


if __name__ == '__main__':
    a = Login
    print(a.url[0])
