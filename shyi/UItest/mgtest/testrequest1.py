from selenium import webdriver
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('w3c', False)
caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(desired_capabilities=caps, options=chrome_options)
driver.get('https://www.baidu.com')
# 重要：获取浏览器请求的信息，包括了每一个请求的请求方法/请求头，requestId等信息
logs = [json.loads(log['message'])['message'] for log in driver.get_log('performance')]
for i in logs:
        print(i)
driver.close()