# -*- coding: utf-8 -*-
# liujun
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from urllib import parse
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'text/html')])
    # environ是当前请求的所有数据，包括Header和URL，body，这里只涉及到get
    # 获取当前get请求的所有数据，返回是string类型
    params = parse_qs(environ['QUERY_STRING'])
    # 获取get中key为name的值
    name = params.get('name', [''])[0]
    password = params.get('password', [''])[0]
    companyCode = params.get('companyCode', [''])[0]
    siteCode = params.get('siteCode', [''])[0]
    client = params.get('client', [''])[0]
    environment = params.get('environment', [''])[0]
    token = get_token(name, password, companyCode, siteCode, client, environment)
    # print(token)
    # 组成一个数组，数组中只有一个字典
    dic = {'name': name, 'token': token}
    # print(dic)
    # print(json.dumps(dic))
    # print([json.dumps(dic)])
    return [json.dumps(dic).encode('utf-8')]
def get_token(username, password, companyCode, siteCode, client, environment):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('w3c', False)
    caps = DesiredCapabilities.CHROME
    caps['loggingPrefs'] = {'performance': 'ALL'}
    driver = webdriver.Chrome(desired_capabilities=caps, options=chrome_options)

    if (client == 'mg'):
        if (environment == 'prod'):
            url = "https://" + client + ".kmelearning.com/" + companyCode + "/" + siteCode + "/login"
        else:
            url = "https://" + environment + "." + client + ".kmelearning.com/" + companyCode + "/" + siteCode + "/login"
        # 操作浏览器，打开url，用户名密码登陆
        print(url)
        driver.get(url)
        driver.find_element_by_id("account").send_keys(username)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_xpath(
            "html/body/div[1]/div/div[2]/div/div[2]/div/form/div[3]/div/div/span/button").click()
        time.sleep(0.5)
        token = driver.execute_script('return sessionStorage.getItem("mgtk");')
        # js = 'window.sessionStorage.clear();'
        # driver.execute_script(js)
    elif (client == 'pc'):
        if (environment == 'prod'):
            url = "https://" + client + ".kmelearning.com/" + companyCode + "/" + siteCode + "/login"
        else:
            url = "https://" + environment + "." + client + ".kmelearning.com/" + companyCode + "/" + siteCode + "/login"
        print(url)
        driver.get(url)
        time.sleep(0.5)
        driver.find_element_by_xpath(
            "html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div[1]/span[1]/input").send_keys(username)
        driver.find_element_by_xpath(
            "html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div[1]/span[2]/input").send_keys(password)
        driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div[1]/button").click()
        time.sleep(0.5)
        token = driver.execute_script('return sessionStorage.getItem("token");')
    else:
        if (environment == 'prod'):
            url = "https://" + client + ".kmelearning.com/#/" + companyCode + "/" + siteCode + "/login"
        else:
            url = "https://" + environment + "." + client + ".kmelearning.com/#/" + companyCode + "/" + siteCode + "/login"
            url2 = "https://" + environment + "." + client + ".kmelearning.com//web-student/api/portal/public/login/view?type=3&companyCode=" + companyCode + "&siteCode=" + siteCode + "&timeStamp=1614736171198&audienceid=&signature=&timestamp=1614736156906&nonce=&signatureversion=&signaturemethod="
        print(url)
        driver.get(url)
        time.sleep(0.5)
        driver.find_element(By.ID, "login-user-input").send_keys(username)
        driver.find_element(By.ID, "login-password-input").send_keys(password)
        driver.find_element(By.XPATH, "html/body/div[1]/div/div[3]/div/div/button").click()
        # driver.find_element_by_id("login-user-input").send_keys(username)
        # driver.find_element_by_id("login-password-input").send_keys(password)
        # driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div/div/button").click()
        time.sleep(1.5)
        token = driver.execute_script('return sessionStorage.getItem(companyCode+"daying");')
        # print(token)
    js = 'window.localStorage.clear();'
    driver.execute_script(js)
    js = 'window.sessionStorage.clear();'
    # 重要：获取浏览器请求的信息，包括了每一个请求的请求方法/请求头，requestId等信息
    driver.execute_script(js)
    logs = [json.loads(log['message'])['message'] for log in driver.get_log('performance')]
    for i in logs:
        print(i)
    return token


if __name__ == "__main__":
    port = 5088
    httpd = make_server("0.0.0.0", port, application)
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    """最终的效果：不会弹出浏览器窗口"""
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()
