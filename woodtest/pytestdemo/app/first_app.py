# -*- coding: UTF-8 -*-
from appium import webdriver
# 字典
#1.设置终端参数项
desire_caps = {
    "platformName":"Android",
    "platformVersion":"5.1.1",
    "deviceName":"iqoo7",
    "appPackage":"com...",
    "appActivity":"com......"
    "noReset":True

}
# 2.appium server进行启动

# 3.发送指令给到appium server
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_caps)


#
