# -*- coding: UTF-8 -*-
import time

from ddt import ddt, data, unpack

from woodtest.threeweb.base.base_util import BaseUtil
from woodtest.threeweb.common.excel_util import ExcelUtil
from woodtest.threeweb.pageobject.login_page import LoginPage

@ddt
class TestLogin(BaseUtil):

    @data(*ExcelUtil().read_excel())
    @unpack
    def test_01_login(self, index, username, password):
        """ 登录 """
        print(index, username, password)
        lp = LoginPage(self.driver)
        lp.login_ecshop(username, password)

        time.sleep(3)
        self.assertEqual(lp.get_except_result(), 'Dashboard')

        # if index == 1:
        #     #断言
        #     self.assertEqual(lp.get_(),"退出")
