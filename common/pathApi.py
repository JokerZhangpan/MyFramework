#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
author：JokerZhang
data: 2019-03-18

对一些使用到的方法进行简单的封装
"""


from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains


def by_id(driver, id):
    """

    :param driver: 浏览器驱动
    :param id: 待定位元素的ID
    :return: 获得元素定位
    """
    try:
        return driver.find_element_by_id(id)
    except NoSuchElementException as e:
        print("无此元素！", e)


def by_ids(driver, id):
    """

    :param driver: 浏览器驱动
    :param id: 待定位元素的ID
    :return: 获得一组元素定位
    """
    try:
        return driver.find_elements_by_id(id)
    except NoSuchElementException as e:
        print("无此元素！", e)


def by_name(driver, name):
    """

    :param driver: 浏览器驱动
    :param name: 待定位元素的name
    :return: 获得元素定位
    """
    try:
        return driver.find_element_by_name(name)
    except NoSuchElementException as e:
        print("无此元素！", e)


def by_names(driver, name):
    """

    :param driver: 浏览器驱动
    :param name: 待定位元素的name
    :return: 获得一组元素定位
    """
    try:
        return driver.find_elements_by_name(name)
    except NoSuchElementException as e:
        print("无此元素！", e)


def by_class_name(driver, class_name):
    """

    :param driver: 浏览器驱动
    :param class_name: 待定位元素的classname
    :return: 获得元素定位
    """
    try:
        return driver.find_element_by_class_name(class_name)
    except NoSuchElementException as e:
        print("无此元素！", e)


def by_class_names(driver, class_name):
    """

    :param driver: 浏览器驱动
    :param class_name: 待定位元素的classname
    :return: 获得一组元素定位
    """
    try:
        return driver.find_elements_by_class_name(class_name)
    except NoSuchElementException as e:
        print("无此元素！", e)


def by_tag_name(driver, tag_name):
    """

    :param driver: 浏览器驱动
    :param tag_name: 待定位元素的tagname
    :return: 获得元素定位
    """
    try:
        return driver.find_element_by_tag_name(tag_name)
    except NoSuchElementException as e:
        print("无此元素！", e)


def by_tag_names(driver, tag_name):
    """

    :param driver: 浏览器驱动
    :param tag_name: 待定位元素的tagname
    :return: 获得一组元素定位
    """
    try:
        return driver.find_elements_by_tag_name(tag_name)
    except NoSuchElementException as e:
        print("无此元素！", e)


def by_link_text(driver, link_text):
    """

    :param driver: 浏览器驱动
    :param link_text: 待定位元素的link_text
    :return: 获得元素定位
    """
    try:
        return driver.find_element_by_link_text(link_text)
    except NoSuchElementException as e:
        print("无此元素！", e)


def by_link_texts(driver, link_text):
    """

    :param driver: 浏览器驱动
    :param link_text: 待定位元素的link_text
    :return: 获得一组元素定位
    """
    try:
        return driver.find_elements_by_link_text(link_text)
    except NoSuchElementException as e:
        print("无此元素！", e)


def by_partial_link_text(driver, partial_link_text):
    """

    :param driver: 浏览器驱动
    :param partial_link_text: 待定位元素的partial_link_text
    :return: 获得元素定位
    """
    try:
        return driver.find_element_by_partial_link_text(partial_link_text)
    except NoSuchElementException as e:
        print("无此元素！", e)


def by_partial_link_texts(driver, partial_link_text):
    """

    :param driver: 浏览器驱动
    :param partial_link_text: 待定位元素的partial_link_text
    :return: 获得一组元素定位
    """
    try:
        return driver.find_elements_by_partial_link_text(partial_link_text)
    except NoSuchElementException as e:
        print("无此元素！", e)


def by_xpath(driver, path):
    """

    :param driver: 浏览器驱动
    :param path: 待定位元素的xpath
    :return: 获得元素定位
    """

    try:
        return driver.find_element_by_xpath(path)
    except NoSuchElementException as e:
        print("无此元素！", e)


def by_xpaths(driver, path):
    """

    :param driver: 浏览器驱动
    :param path: 待定位元素的xpath
    :return: 获得一组元素定位
    """

    try:
        return driver.find_elements_by_xpath(path)
    except NoSuchElementException as e:
        print("无此元素！", e)


def by_css_selector(driver, css):
    """

    :param driver: 浏览器驱动
    :param css: 待定位元素的css
    :return: 获得元素定位
    """

    try:
        return driver.find_element_by_css_selector(css)
    except NoSuchElementException as e:
        print("无此元素！", e)


def by_css_selectors(driver, css):
    """

    :param driver: 浏览器驱动
    :param css: 待定位元素的css
    :return: 获得一组元素定位
    """

    try:
        return driver.find_elements_by_css_selector(css)
    except NoSuchElementException as e:
        print("无此元素！", e)


def is_element_present(driver, how, what):
    """

    :param driver: 浏览器驱动
    :param how: 元素属性标签
    :param what: 元素属性名字
    :return: 存在为True，不存在False
    """

    try:
        driver.find_element(by=how, value=what)
    except NoSuchElementException as e:
        print("无此元素! ", e)
        return False
    return True


def is_alert_present(driver):
    """

    :param driver: 浏览器驱动
    :return: 存在返回True，不存在返回False
    """

    try:
        driver.switch_to.alert
    except NoAlertPresentException:
        return False
    return True


def close_alert_and_get_its_text(driver, accept_next_alert):
    """

    :param driver: 浏览器驱动
    :param accept_next_alert: 获取alert标志位
    :return: 获取弹窗内容并返回next_alert确认标志位
    """

    try:
        alert = driver.switch_to.alert()
        alert_text = alert.text

        if accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        print(alert_text)
    finally:
        accept_next_alert = True
        return accept_next_alert


def mouse_actions(driver,mouse_action):
    """

    :param driver: 浏览器驱动
    :param mouse_action: 鼠标行为，比如：右击、双击
    :return: 执行结果
    """

    return ActionChains(driver).context_click(mouse_action).perform()


def mouse_drag_and_drop(driver, element_path, target):
    """

    :param driver: 浏览器驱动
    :param element_path: 元素原path
    :param target: 元素待移动到path
    :return: 执行结果
    """

    return ActionChains(driver).drag_and_drop(element_path, target).perform()


def mouse_move_to_element(driver, element_path):
    """

    :param driver: 浏览器驱动
    :param element_path: 待悬浮的元素path
    :return: 执行结果
    """
    return ActionChains(driver).move_to_element(element_path).perform()


def send_keys(path, *key):
    """

    :param path: 待操作元素的path
    :param key: 模拟按键
    :return: 执行结果
    """

    return path.send_keys(key)


"""
expected_conditions 提供的预期条件判断方法


title_is
title_contains
presence_of_element_located  判断元素是否被加载DOM树中，并不代表元素一定可见。
visibility_of_element_located   判断元素是否可见（可见表示元素非隐藏，并且元素的宽和高都不等于0）
visibility_of   判断元素是否可见，接收参数为定位后的元素
is_displayed   判断元素是否可见
present_of_all_elements_located 判断是否至少有一个元素存在于DOM树中。
text_to_be_present_in_element   判断某个元素中的text是否包含了预期的字符串
text_to_be_present_in_element_value 判断某个元素中得value是否包含了预期的字符串
frame_to_be_available_and_switch_to_it  判断表单是否能切换进去，如果可以返回True并且switch进去，否则返回False
invisibility_of_element_located 判断某个元素是否不存在于DOM树或不可见
element_to_be_clickable     判断元素是否可见并可点击
staleness_of  等到一个元素从DOM树中移除
element_to_be_selected  判断某个元素是否被选中，一般不用在下拉列表
element_selection_state_to_be   判断某个元素（定位后的元素）得选中状态是否符合预期
element_located_selection_state_to_be   判断耨个元素的选中状态是否符合预期，接收的参数为定位path
alert_is_present    判断页面上是否存在alert


window_handles  获取所有窗口的句柄
current_window_handle   获取当前窗口的句柄


switch_to.frame()   切换到frame
switch_to.parent_content()  跳出当前frame到上一级
switch_to.default_content() 跳回最外层的页面
"""


