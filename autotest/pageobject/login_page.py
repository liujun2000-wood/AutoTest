# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By

from woodtest.threeweb.base.base_page import BasePage
from woodtest.threeweb.common.logger import Logger


class LoginPage(BasePage):
    # 页面元素（类属性）
    username_loc = (By.ID, "account")
    password_loc = (By.ID, "password")
    submit_loc = (By.XPATH, "//button[span[text()='登 录']]")
    Dashboard_loc = (By.XPATH, "//*[@class='logoText__2ej_q']")

    # 页面动作
    def login_ecshop(self, username='qatest1', password="11111"):
        # self.locator_element(LoginPage.username_loc).send_keys("qatest1")
        # self.locator_element(LoginPage.password_loc).send_keys("11111")
        try:
            self.send_keys(LoginPage.username_loc, username)
            Logger().getlog().info("元素定位成功，元素："+"username元素")
        except Exception as error:
            Logger().getlog().error("元素定位失败，元素："+str(error))
        self.send_keys(LoginPage.password_loc, password)
        self.click(LoginPage.submit_loc)

    # 断言
    def get_except_result(self):
        try:
            Dashboard = self.get_value(LoginPage.Dashboard_loc)
            Logger().getlog().info("登录成功找到Dashboard")
        except Exception as error:
            Logger().getlog().error("登录失败未找到Dashboard" + str(error))
        return Dashboard



