# -*- coding: UTF-8 -*-
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from woodtest.pytestdemo.emails.email_manage import EmailManage

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./', '*.py')
    files = open('./report.html','wb')
    runner = HTMLTestRunner(stream=files,  title='自动化测试报告', description='报告描述')
    runner.run(suite)
    files.close()  # 在发送前一定要把文件流关闭
    # 发送邮件
    time.sleep(3)
    EmailManage().send_email(files.name)