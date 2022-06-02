# -*- coding: UTF-8 -*-
import os

import pytest
import requests

from woodtest.pytestdemo import YamlUtil


class TestApi:

    # @pytest.mark.parametrize('companyCode, siteCode, accountId', [['shyz', 'shyz', '1314'], ['shyz', 'shyz', '1387228507406544896'], ['shyz', 'shyz', '1387228507410739200']])
    @pytest.mark.parametrize('args', YamlUtil(os.getcwd()+'/testcase/test_api.yaml').read_yaml())
    def test_01_login(self, args):
        print(args)
        url = args['request']['url']
        params = args['request']['params']
        h = args['request']['headers']
        res = requests.get(url, params=params, headers= h)
    #     url = 'https://uat.wechat.kmelearning.com/system/public/pressure/test/get/token'
    #     params = {
    #         "companyCode":"shyz",
    #         "siteCode":"shyz",
    #         "accountId":"1314"
    #     }
    #     h = {"Content-Type": "application/json"}
    #     # print("执行了没有")
    #     res = requests.get(url, params=params, headers=h)
        print(res.json())
        print(args['validate'])
        # 断言
        for val in args['validate']:
            print(val['eq'])
        # assert args['validate']['eq'][0] in res.text



