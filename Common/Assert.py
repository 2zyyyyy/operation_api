# @File:Assert.py
# @Author:2zyyyyy
# @Time:2019年03月07日
# @Explain: 封装Assert
import json

from Common import Log
from Common import Consts


class Assertions:
    def __init__(self):
        self.log = Log.MyLog()

    def assert_code(self, code, expected_code):
        """
        验证request状态码
        :param code:
        :param expected_code:
        """
        try:
            assert code == expected_code
            return True
        except Exception:
            self.log.error('status code error,expected_code is %s,status code is %s' % (expected_code, code))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证request body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True
        except Exception:
            self.log.error('Response body msg != expected_msg, expected_msg is %s, body_msg is %s' % (expected_msg,
                                                                                                      body_msg))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        """
        # noinspection PyBroadException
        try:
            text = json.dumps(body, ensure_ascii=False)  # json.dumps序列化时对中文默认的ascii编码.想输出真正的中文需要指定False
            print(text)
            assert expected_msg in text
            return True
        except Exception:
            self.log.error('Response body Does not contain expected_msg, expected_msg is %s' % expected_msg)
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        """
        # noinspection PyBroadException
        try:
            assert body == expected_msg
            return True
        except Exception:
            self.log.error('Response body != expected_msg, expected_msg is %s, body is %s' % (expected_msg, body))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间，单位:ms
        :param time:
        :param expected_time:
        """
        # noinspection PyBroadException
        try:
            assert time < expected_time
            return True
        except Exception:
            self.log.error('Response time > expected_time, expected_time is %s, time is %s' % (expected_time, time))
            Consts.RESULT_LIST.append('fail')

            raise
