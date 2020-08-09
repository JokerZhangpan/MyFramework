#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
author: JokerZhang
data: 2018-03-18
description: 运行测试脚本，并生成测试报告，以及发送邮件。
"""

from common import generateReport
from common import findNewReport
from case.test_baidu import Baidu
from common import sendMail
import os
import unittest

test_report = os.path.dirname(os.path.abspath(__file__)) + "/report"
test_dir = os.path.dirname(os.path.abspath(__file__)) + "/case"

# 使用discover执行所有测试脚本
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

if __name__ == '__main__':

    # 使用测试套件执行想要运行的脚本
    # suite = unittest.TestSuite()
    # suite.addTest(Baidu("test_search_selenium_ide"))
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # ——————————————————————————————————————
    # 通过获取类里所有的测试脚本放入测试套件中运行脚本
    # tests = unittest.TestLoader().loadTestsFromTestCase(Baidu)
    # suite = unittest.TestSuite(tests)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    generateReport.generate_report(test_report, discover)
    new_report = findNewReport.new_report(test_report)
    sendMail(new_report)








