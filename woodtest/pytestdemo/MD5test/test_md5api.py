# -*- coding: UTF-8 -*-
import hashlib
import unittest
import requests


class TestNd5Api(unittest.TestCase):

    def test_01_login(self):
        """
        测试登录接口
        :return:
        """
        url = 'http://127.0.0.1:5000/get_token'
        username = hashlib.md5('admin'.encode('utf-8')).hexdigest()
        password = hashlib.md5('123'.encode('utf-8')).hexdigest()
        data = {
            'username': str(username).upper(),
            'password': str(password).upper()
        }
        res = requests.post(url=url, data=data)
        result = res.json()
        # 断言
        self.assertEqual(res.status_code,200)
        self.assertEqual(result['error_code'], '1000')
        self.assertEqual(result['message'], '登录成功')