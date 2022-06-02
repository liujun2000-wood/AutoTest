# -*- coding: utf-8 -*- 
# @Time : 2020/12/12 11:19 
# @Author : Aries 
# @Site :  
# @File : login.py 
# @Software: PyCharm
# liujun
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

import requests
# from login import login
driver = webdriver.Chrome()
url='https://wechat.kmelearning.com/#/fulan/yy2/login'
def get_token(username, password):
    chrome_options = Options()
    chrome_options.add_experimental_option('w3c', False)
    chrome_options.add_argument('--log-level=1')  # 忽略错误
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument('--ignore-certificate-errors')  # 忽略证书错误
    chrome_options.add_argument('--headless')  # 开启无头模式
    chrome_options.add_argument('--disable-gpu')

    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=1920x1080")  # I added this
    caps = {
        'browserName': 'chrome',
        'loggingPrefs': {
            'browser': 'ALL',
            'driver': 'ALL',
            'performance': 'ALL',
        },
        'goog:chromeOptions': {
            'perfLoggingPrefs': {
                'enableNetwork': True,
            },
            'w3c': False,
        },
    }

    driver = webdriver.Chrome(desired_capabilities=caps, options=chrome_options)

    driver.get(url)
    time.sleep(0.5)
    # driver.find_element(By.ID, "login-user-input").send_keys(username)
    driver.find_element_by_id("login-user-input").send_keys(username)
    driver.find_element(By.ID, "login-password-input").send_keys(password)
    driver.find_element(By.XPATH, "html/body/div[1]/div/div[3]/div/div/button").click()
    time.sleep(0.5)

    logs = [json.loads(log['message'])['message'] for log in driver.get_log('performance')]
    for i in logs:
        print(i)
    # 获取token的方法：　　
    ''' 
        1、要从Local Storage中获取还是要从Session Storage中获取，具体看目标系统存到哪个中-----开发者模式查看
       2、window.SessionStorage和直接写SessionStorage是等效的
       3、一定要使用return，不然获取到的一直是None
       4、get的Item不一定就叫token，得具体看目标系统把token存到哪个变量中　　
    '''
    time.sleep(2.5)

    def get_chrome_by_proxy():
        """
        获取谷歌浏览器对象(代理启动)
            :return:谷歌浏览器对象
        """
        service.command_line_args()
        # 启动浏览器驱动
        service.start()
        # 创建谷歌浏览器插件
        plugin_path = create_proxyauth_extension(
            proxy_host=CONFIG["proxy_host"],
            proxy_port=int(CONFIG["proxy_port"]),
            proxy_username=CONFIG["proxy_user"],
            proxy_password=CONFIG["proxy_pwd"]
        )
        options = Options()
        options.add_argument("--start-maximized")
        # options.add_argument('--incognito')                     # 配置浏览器主题为黑色
        options.add_argument('--ignore-certificate-errors')  # 忽略连接警告信息
        options.add_experimental_option("detach", True)  # 不自动关闭浏览器
        options.add_argument("--disable-gpu")  # 禁用gpu
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 禁止加载图片
        options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 禁用浏览器正在被自动化程序控制的提示
        options.add_experimental_option('useAutomationExtension', False)  # 禁用扩展插件
        options.add_experimental_option('w3c', False)
        caps = {
            'loggingPrefs': {
                'performance': 'ALL',
            }
        }
        options.add_extension(plugin_path)
        # options.add_experimental_option('prefs', prefs)
        return webdriver.Chrome(options=options, desired_capabilities=caps)
    request_log = driver.get_log('performance')
    print(request_log)

    token = driver.execute_script('return sessionStorage.getItem("fulandaying");')


    # driver.close()#close只会关闭当前页面
    driver.quit()#quit会退出驱动并且关闭所关联的所有窗口
    return token



print(get_token("yaya01","Aa123456"))




