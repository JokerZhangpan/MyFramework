#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
author：JokerZhang
data: 2019-03-18
description: 登录函数，难点在获取path。如果通过ID找不到可以修改为其他方式获取path。
"""
from common import pathApi
from selenium.common.exceptions import NoSuchElementException
import time


def login(username, userpwd, *path):
    """
    username: 用户名
    userpwd: 密码
    *path: 可变参数，可填多个path。

    """

    try:
        pathApi.byId(path).clear()
        pathApi.byId(path).send_keys(username)

        pathApi.byId(path).clear()
        pathApi.byId(path).send_keys(userpwd)

        pathApi.byId(path).click()
        time.sleep(3)

    except NoSuchElementException as e:
        print("无此控件!", e)
    except Exception as err:
        print("此处发生错误", err)





