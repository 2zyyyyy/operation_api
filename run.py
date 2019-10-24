# @File:run.py
# @Author:2zyyyyy
# @Time:2019年03月05日
# @Explain: 运行用例集

import sys
import pytest

from Common import Log
from Common import Shell
from Config import Config

if __name__ == '__main__':
    conf = Config.Config()
    log = Log.MyLog()
    log.info('初始化配置文件, path=' + conf.conf_path + '\n')

    shell = Shell.Shell()
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    # 定义测试集
    # allure_list = '--allure_features=Home,Personal'

    args = ['-s', '-q', '--alluredir', xml_report_path, '--clean']
    # log.info('执行用例集为：%s' % allure_list)
    # self_args = sys.argv[1:]
    pytest.main(args)
    cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path + ' --clean')

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise
