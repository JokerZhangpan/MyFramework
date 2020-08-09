#!/usr/python3
# -*- coding:utf-8 -*-
"""
author: JokerZhang
data: 2019-03-18
"""

from email.mime.text import MIMEText
from email.header import Header
import smtplib

stmp_server = "smtp.xxx.xxx"
send_user_name = "xxx@xxx.xxx"
send_user_pwd = "xxxx"
recieve_users = ['xxx@xxx.xxx', 'xxx@xxx.xxx']


def sendmail(file_new):
    """
    :param file_new: 获取到的最新测试报告
    :return: 无
    """

    f = open(file_new, 'r')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')

    smtp = smtplib.SMTP()
    try:
        smtp.connect(stmp_server, 25)
        smtp.login(send_user_name, send_user_pwd)
    except Exception as e:
        print("邮箱服务器处发生错误: " + e)
    smtp.sendmail(send_user_name, recieve_users, msg.as_string())
    smtp.quit()
    print('邮件发送成功！')
