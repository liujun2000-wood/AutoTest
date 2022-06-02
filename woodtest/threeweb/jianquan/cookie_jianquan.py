# -*- coding: UTF-8 -*-
import re
import unittest

import  requests

class CookieJianquan(unittest.TestCase):

    csrf_token = ""
    csrf_cookie = ""
    session = requests.session()

    def test_goto_index(self):
        url = ""

        # res = requests.get(url)
        res = CookieJianquan.session.get(url=url)
        print(res.text)
        # 通过正则表达式获取token
        value = re.search('(.+?)', res.text)
        CookieJianquan.csrf_token = value.group(1)
        CookieJianquan.csrf_cookie = res.cookies


    def test_login_phowd(self):
        url = ""
        data = {}
        headers ={}

        res = requests.post(url=url, data=data, headers=headers, cookies=CookieJianquan.csrf_cookie)
        print(res.text)


