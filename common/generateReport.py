#!/usr/python3
# -*- coding:utf-8 -*-
"""
author: JokerZhang
data: 2019-03-18
"""

import time
from HTMLTestRunner import HTMLTestRunner


def generate_report(test_report, suite):
    """
    :test_dir: 测试脚本目录
    :test_report: 测试报告目录
    :return:无
    :description: 运行所有的测试用例后生成测试报告
    """

    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = test_report + "/" + now + "report.html"

    with open(filename, 'w') as file:
        file.write('\n')
        runner = HTMLTestRunner(stream=file, report_title='测试报告', descriptions='用例执行情况')
        runner.run(suite)





