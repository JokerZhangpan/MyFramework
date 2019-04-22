#!/usr/python3
# -*- coding:utf-8 -*-
"""
author: JokerZhang
data: 2019-03-18
"""

import os


def new_report(test_report):
    """

    :param test_report: 测试报告存放路径
    :return: 最新的测试报告
    :description: 在所有的测试报告中找到时间最新的报告
    """

    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "/" + fn))
    newreport = os.path.join(test_report, lists[-1])

    return newreport
