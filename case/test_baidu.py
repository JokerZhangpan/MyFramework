#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
author: JokerZhang
data: 2019-03-18
"""

from selenium import webdriver
from common import pathApi
import unittest
import time

base_url = "http://www.baidu.com"


class Baidu(unittest.TestCase):

    """百度搜索"""

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = base_url
        self.veritificationErrors = []
        self.accept_next_alert = True

    def test_search_selenium_ide(self):

        """搜索关键字：selenium ide"""

        driver = self.driver
        driver.get(self.base_url)

        pathApi.by_id(driver, "kw").clear()
        pathApi.send_keys(pathApi.by_id(driver, "kw"), "selenium ide")
        time.sleep(1)

        pathApi.by_id(driver, "su").click()
        time.sleep(1)

        pathApi.is_alert_present(driver)
        pathApi.is_element_present(driver, "name", "wd")
        pathApi.close_alert_and_get_its_text(driver, self.accept_next_alert)

    def test_search_setting(self):

        """修改搜索设置"""

        driver = self.driver
        driver.get(self.base_url)

        pathApi.mouse_move_to_element(driver, pathApi.by_link_text(driver, "设置"))
        pathApi.by_link_text(driver, "搜索设置").click()
        pathApi.by_link_text(driver, "保存设置").click()
        time.sleep(1)

        if pathApi.is_alert_present(driver):
            pathApi.close_alert_and_get_its_text(driver, self.accept_next_alert)

    def tearDown(self):

        self.driver.quit()
        self.assertEqual([], self.veritificationErrors)


if __name__ == "__main__":

    unittest.main()
