# -*- coding: UTF-8 -*-
import time

from woodtest.threeweb.base.base_util import BaseUtil
from woodtest.threeweb.pageobject.login_page import LoginPage


class TestLogin(BaseUtil):

    def test_01_login(self):
        """ 登录 """
        lp = LoginPage(self.driver)
        lp.login_ecshop()
        # 断言
        time.sleep(3)
        self.assertEqual(lp.get_except_result(), 'Dashboard')

    # def test_02_login(self):
    #     """ 登录2 """
    #     lp = LoginPage(self.driver)
    #     lp.login_ecshop('qatest2', '11111')



