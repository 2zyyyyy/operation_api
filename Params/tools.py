# @File:tools.py
# @Author:2zyyyyy
# @Time:2019年04月15日
# @Explain: 读取yaml测试数据

import yaml
import os
import os.path
import pprint


def parse():
    yaml_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/Params/Yaml'
    pages = {}
    for root, dirs, files in os.walk(yaml_path):
        for name in files:
            watch_file_path = os.path.join(root, name)
            with open(watch_file_path, 'r') as f:
                page = yaml.safe_load(f)
                pages.update(page)
        return pages


class GetPages:
    @staticmethod
    def get_page_list():
        _page_list = {}
        pages = parse()
        for page, value in pages.items():
            parameters = value['parameters']
            data_list = []

            for parameter in parameters:
                data_list.append(parameter)
            _page_list[page] = data_list
            # pprint.pprint(_page_list)

        return _page_list


if __name__ == '__main__':
    lists = GetPages.get_page_list()
