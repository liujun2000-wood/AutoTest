# -*- coding: UTF-8 -*-
import time
import unittest

from selenium import webdriver
from autotest.common.logger import Logger


class BaseUtil(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 创建logger对象
        cls.lu = Logger()
        cls.logger = cls.lu.getlog()


    def setUp(self) -> None:
        self.logger.info("----------------测试用例开始执行------------")
        global driver
        # 打开浏览器
        self.driver = webdriver.Chrome()
        driver = self.driver
        # 加载网页
        self.driver.get("https://test.mg.kmelearning.com/shyz/shyz/login")

    def tearDown(self):
        self.logger.info("----------------测试用例开始结束------------\n")
        time.sleep(3)
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        # 移除日志处理器
        pass




