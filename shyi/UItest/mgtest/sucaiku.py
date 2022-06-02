# -*- coding: utf-8 -*- 
# @Time : 2020/12/13 11:26 
# @Author : Aries 
# @Site :  
# @File : sucaiku.py 
# @Software: PyCharm
# liujun
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
# from login import login
browser = webdriver.Chrome()
browser.get('https://uat.mg.kmelearning.com/shyz/shyz/login')
browser.maximize_window()
browser.find_element_by_id("account").send_keys("shyz")
browser.find_element_by_id("password").send_keys("Dfcv3344")
browser.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/div/form/div[3]/div/div/span/button").click()
time.sleep(1)

browser.get('https://uat.mg.kmelearning.com/shyz/shyz/index/online/material-management')
time.sleep(1)


# 删除之前创建
# browser.find_element_by_xpath("html/body/div[1]/section/div/main/div/div/div/div/div[3]/div/div/div/div/div/div/table/tbody/tr[1]/td[8]/span/a[2]").click()
# browser.find_element_by_xpath("html/body/div[2]/div/div/div/div[2]/div/div/div[2]/button[1]").click()
# time.sleep(1)
# browser.find_element_by_xpath("html/body/div[1]/section/div/main/div/div/div/div/div[3]/div/div/div/div/div/div/table/tbody/tr[1]/td[8]/span/a[2]").click()
# browser.find_element_by_xpath("html/body/div[2]/div/div/div/div[2]/div/div/div[2]/button[2]").click()

browser.find_element_by_xpath("html/body/div[1]/section/div/main/div/div/div/div/div[2]/a/button").click()
time.sleep(1)
browser.find_element(By.ID, "name").send_keys("素材名称")
browser.find_element_by_xpath("html/body/div[1]/section/div/main/div/div/div/div/form/div[2]/div[2]/div/span/div/div/div").click()
browser.find_element_by_xpath("html/body/div[2]/div/div/div/ul/li[1]").click()
browser.find_element_by_xpath("html/body/div[1]/section/div/main/div/div/div/div/form/div[3]/div[2]/div/span/div/div").click()
browser.find_element_by_xpath("html/body/div[3]/div/div/div/ul/li[3]").click()

# browser.find_element_by_xpath("html/body/div[1]/section/div/main/div/div/div/div/form/div[4]/div[1]/div[2]/div/span/span/div[1]/span/button").click()
# browser.find_element_by_xpath("html/body/div[1]/section/div/main/div/div/div/div/form/div[4]/div[1]/div[2]/div/span/span/div[1]/span/button").send_keys("D:\\tool\\[优]敏捷测试与开发之我见.pdf")
browser.find_element_by_id("upload").send_keys("D:\\tool\\[优]敏捷测试与开发之我见.pdf")
time.sleep(1)
browser.find_element(By.ID, "textHour").send_keys("0")
browser.find_element(By.ID, "textMinute").send_keys("2")
browser.find_element(By.ID, "textSecond").send_keys("10")
browser.find_element(By.ID, "producer").send_keys("制作人")
browser.find_element_by_xpath("html/body/div[1]/section/div/main/div/div/div/div/form/div[5]/button[1]").click()
browser.close()