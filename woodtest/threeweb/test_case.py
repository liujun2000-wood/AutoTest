# -*- coding: UTF-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(unittest.TestCase):
    def test_01_login(self):
        #全局变量，不关闭浏览器
        global driver
        # 打开浏览器
        driver = webdriver.Chrome()
        # 加载网页
        driver.get("https://test.mg.kmelearning.com/shyz/shyz/login")
        # 定位元素
        # 不利于封装，自动化中基本不用
        # driver.find_element_by_id("kw")
        # 利于封装
        driver.find_element(By.ID,  "account").send_keys("qatest1")
        driver.find_element(By.ID,  "password").send_keys("11111")
        driver.find_element(By.XPATH, "//button[span[text()='登 录']]").click()
        driver.implicitly_wait(10)

        #处理弹窗:alert(只有确定),confirm(有确定有取消),prompt(有确定有取消还可以输入值)
        time.sleep(3)
        ale = driver.switch_to.alert
        ale.accept()
        ale.dismiss()
        ale.text
        ale.send_keys()
        #accept点击确定，dismiss点击取消，text获得文本，send_keys输入值
    # dirver.get("https://test.mg.kmelearning.com/shyz/shyz/index/tool/test/testbase-management")





