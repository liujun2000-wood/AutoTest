# -*- coding: utf-8 -*- 
# @Time : 2020/12/16 13:42 
# @Author : Aries 
# @Site :  
# @File : gettoken.py 
# @Software: PyCharm
# liujun
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#浏览器模式设置
"""
#1 谷歌浏览器设置为无头模式
opts = webdriver.ChromeOptions()    # 声明一个谷歌配置对象
opts.set_headless()
# 设置成无头
driver = webdriver.Chrome(chrome_options=opts)
# 选项注入
chrome_options = Options()
chrome_options.add_argument('--headless')
#最终的效果：不会弹出浏览器窗口
driver = webdriver.Chrome(options=chrome_options)
"""
opts = Options()
opts.headless = True  # 设置无头模式，相当于执行了opt.add_argument('--headless')和opt.add_argument('--disable-gpu')(--disable-gpu禁用gpu加速仅windows系统下执行)。
driver = webdriver.Chrome(options=opts)  # 如果没有将chromedriver加入环境变量，第一个参数需传入其绝对路径

# driver = webdriver.Chrome()

url = "https://uat.mg.kmelearning.com/shyz/shyz/login"
def get_token(username, password):
    #操作浏览器，打开url，用户名密码登陆
    driver.get(url)
    driver.find_element_by_id("account").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/div/form/div[3]/div/div/span/button").click()
    time.sleep(0.5)
    # cookie_items = driver.get_cookies()
    # cookie_str = ""
    # print('cookie_items:', cookie_items)
    #
    # # 组装cookie字符串
    # for item_cookie in cookie_items:
    #     item_str = item_cookie["name"] + "=" + item_cookie["value"] + "; "
    #     cookie_str += item_str
    # return cookie_str

    # 获取token的方法：　　
    '''    1、要从Local Storage中获取还是要从Session Storage中获取，具体看目标系统存到哪个中-----开发者模式查看
       2、window.SessionStorage和直接写SessionStorage是等效的
       3、一定要使用return，不然获取到的一直是None
       4、get的Item不一定就叫token，得具体看目标系统把token存到哪个变量中　　
    '''
    token = driver.execute_script('return sessionStorage.getItem("mgtk");')
    # token = driver.execute_script('SessionStorage.getItem("mgtk")')
    # print(token)

    # driver.close()#close只会关闭当前页面
    driver.quit()#quit会退出驱动并且关闭所关联的所有窗口
    return token



print(get_token("shyz","Ghbn7788"))