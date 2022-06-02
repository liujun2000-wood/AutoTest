# -*- coding: UTF-8 -*-

import pytest
from ddt import ddt, data

from woodtest.threeweb import BaseUtil


@ddt
class TestCase(BaseUtil):

    @data({1, "qatest1", "11111"})
    # #  *表示解析掉[]
    # @unpack
    @pytest.mark.run(order=1)
    def test_01_login(self, args):
        print(args)
    # def test_01_login(self, index, username, password):
    #     """ 登录 """
    #     print(index, username, password)
    #     lp = LoginPage(self.driver)
    #     lp.login_ecshop(username, password)
    #     # if index == 1:
    #     #     #断言
    #     #     self.assertEqual(lp.get_(),"退出")
    # @data(*ExcelUtil().read_excel())



