# -*- coding: UTF-8 -*-
import unittest

from selenium import webdriver


class BaseUtil(unittest.TestCase):
    def setUp(self) -> None:
        global driver
        # 打开浏览器
        self.driver = webdriver.Chrome()
        driver = self.driver
        # 加载网页
        self.driver.get("https://test.mg.kmelearning.com/shyz/shyz/login")

    def tearDown(self) -> None:
        driver.quit()



