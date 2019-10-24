# @File:Shell.py
# @Author:2zyyyyy
# @Time:2019年04月28日
# @Explain: 封装执行shell语句方法

import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o
