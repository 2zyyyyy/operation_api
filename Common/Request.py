# @File:Request.py
# @Author:2zyyyyy
# @Time:2019年03月12日
# @Explain: 封装request
import json
import os
import random
import requests
from requests_toolbelt import MultipartEncoder
from Common import Consts
from Common import Token


class Request:

    def __init__(self, env):
        self.token = Token.Token()
        self.get_token = self.token.get_token(env)

    @staticmethod
    def get_request(url, data, header):
        """
        get请求
        :param url:
        :param data:
        :param header:
        :return: response_dicts
        """
        # startswith方法用于检查字符串是否是以指定子字符串开头，是返回True，否返回False。如果参数 beg 和 end 指定值，则在指定范围内检查。
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            # print(url)
        # noinspection PyBroadException
        try:
            if data is None:
                response = requests.get(url=url, headers=header)
            else:
                response = requests.get(url=url, params=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url:', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url:', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Consts.STRESS_LIST.append(time_consuming)

        # 存放接口响应信息
        response_dicts = dict()
        response_dicts['code'] = response.status_code

        # noinspection PyBroadException
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    @staticmethod
    def post_request(url, data, header):
        """
        post请求
        :param url:
        :param data:
        :param header:
        :return: response_dicts
        """
        # startswith方法用于检查字符串是否是以指定子字符串开头，是返回True，否返回False。如果参数 beg 和 end 指定值，则在指定范围内检查。
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            # print(url)
        # noinspection PyBroadException
        try:
            if data is None:
                response = requests.post(url=url, headers=header)
            else:
                response = requests.post(url=url, data=json.dumps(data), headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url:', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url:', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Consts.STRESS_LIST.append(time_consuming)

        # 存放接口响应信息
        response_dicts = dict()
        response_dicts['code'] = response.status_code

        # noinspection PyBroadException
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    @staticmethod
    def post_request_multipart(url, data, header, file_parm, file, file_type):
        """
        提交Multipart/form-data 格式的Post请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :param file_type:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            # print(url)
        try:
            if data is None:
                response = requests.post(url=url, headers=header)
            else:
                data[file_parm] = os.path.basename(file), open(file, 'rb'), file_type

                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )

                header['Content-Type'] = enc.content_type
                response = requests.post(url=url, data=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()

        Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    @staticmethod
    def put_request(url, data, header):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            if data is None:
                response = requests.put(url=url, headers=header)
            else:
                response = requests.put(url=url, data=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()

        Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts
