# -*- coding: utf-8 -*- 
# @Time : 2020/12/16 20:57 
# @Author : Aries 
# @Site :  
# @File : aaa.py 
# @Software: PyCharm
# liujun

from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.sogou.com/')
cookies = driver.get_cookies()  # 获得所有cookie 信息
print('删除前cookies：',cookies)  # 打印cookie信息
driver.add_cookie({'name': 'key-name', 'value': 'value-123456'})  #添加cookie信息
print('key-name cookie信息：',driver.get_cookie('key-name')) # 查看添加的key-name的cookie信息
driver.delete_cookie("key-name")  # 删除一个特定的cookie
driver.delete_all_cookies()  # 删除所有cookie
print('删除后cookies：',driver.get_cookies())
driver.quit()