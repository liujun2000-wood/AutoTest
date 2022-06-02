# -*- coding: UTF-8 -*-
import json
import re

import pytest
import requests

from woodtest.pytestdemo.cookiess.read_extract import ReadExtract


class TestCookie:

    # 类变量
    Authorization = ""
    Authorization1 = ""
    csrf_cookie = ""

    def test_01_start(self):
        url = "https://wechat.kmelearning.com/system/public/pressure/test/get/token?companyCode=fulan&siteCode=fulan&accountId=1016273921890463744"
        res = requests.get(url=url)
        print(res.text)
        # 代码中使用正则表达式
        value = re.search('"data":"(.+?)"', res.text)
        print(value.group(1))
        # 把token保存到全局变量
        TestCookie.Authorization = value.group(1)
        # json.loads()  # 反序列化，把json字符串转换成dict对象
        # json.dumps()  # 序列化，把dict字符串转换成json对象
        result_dict = json.loads(res.text)
        TestCookie.Authorization1 = result_dict['data']
        # 把字典格式的token写到yaml文件中
        # token_dict ={'Authorization':result_dict['data']}
        token_dict = {'Authorization': value.group(1)}
        ReadExtract().write_extract(token_dict)

        # 获取cookie
        TestCookie.csrf_cookie = res.cookies


    def test_02_checkToken(self):
        url = "https://wechat.kmelearning.com/system/api/checkToken?companyCode=fulan&siteCode=fulan"
        data ={
            "authorization": TestCookie.Authorization,
            "terminalType": "1"
        }
        headers ={
            "Connection": "keep-alive",
            "Host": "mg.kmelearning.com",
            "Accept": "application/json,text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": TestCookie.Authorization
        }
        # resp = requests.post(url=url, json=data, headers=headers, cookies=TestCookie.csrf_cookie)
        resp = requests.post(url=url, json=data, headers=headers)
        print(resp.text)


    def test_03_get_site(self):
        url = "https://mg.kmelearning.com/system/manage/site/get?&companyCode=fulan&siteCode=fulan"
        headers ={
            "Connection": "keep-alive",
            "Host": "mg.kmelearning.com",
            "Accept": "application/json,text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": TestCookie.Authorization1
        }
        resp = requests.get(url=url,headers=headers)
        print(resp.text)

    # def test_03_classifysave(self):
    #     url = "https://mg.kmelearning.com/web-manage/manage/classify/save?&companyCode=fulan&siteCode=fulan"
    #     headers = {
    #         "Connection": "keep-alive",
    #         "Host": "mg.kmelearning.com",
    #         "Accept": "application/json,text/plain, */*",
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0",
    #         "Accept-Encoding": "gzip, deflate, br",
    #         "Content-Type": "application/json;charset=UTF-8",
    #         "Authorization": TestCookie.Authorization
    #     }
    #     data = {
    #         "name": "测试课程分类一级",
    #         "description": "测试课程分类一级"
    #     }
    #     resp = requests.post(url=url, json=data, headers=headers)
    #     print(resp.text)


if __name__ == '__main__':
    pytest.main(['-vs'])
