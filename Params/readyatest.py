# @File:readyatest.py
# @Author:2zyyyyy
# @Time:2019年04月15日
# @Explain: 读取yaml文件数据测试

import yaml
import os
import pprint

# 先找到yaml文件路径
yaml_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/Params/Yaml/readya.yaml'
print(yaml_path)
# 打开yaml文件
f = open(yaml_path)
# 读取
yaml_content = yaml.load(f)
f.close()
pprint.pprint(yaml_content)