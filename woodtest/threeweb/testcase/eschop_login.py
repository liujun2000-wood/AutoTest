# -*- coding: UTF-8 -*-
import os
import unittest

import pytest


class EschopLogin(unittest.TestCase):
    age =18

    @unittest.skip("这个用例不执行")
    @pytest.mark.skipif(age>=18,reason="成年")
    def test01_login(self):
        # raise Exception("自定义异常")
        # self.assertTrue(0)
        print("测试登录")

    @pytest.mark.smoke
    @pytest.mark.skip(reason="跳过原因")
    def test02_login2(self):
        print("测试登录2")
        print(ord('A'))

