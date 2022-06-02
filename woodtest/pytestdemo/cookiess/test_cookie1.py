# -*- coding: UTF-8 -*-

import pytest
import requests

from woodtest.pytestdemo.cookiess.read_extract import ReadExtract


class TestCookie:




    def test_04_get_site(self):
        url = "https://mg.kmelearning.com/system/manage/site/get?&companyCode=fulan&siteCode=fulan"
        Authorization = ReadExtract().read_extract()['Authorization']
        headers ={
            "Connection": "keep-alive",
            "Host": "mg.kmelearning.com",
            "Accept": "application/json,text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": Authorization
        }
        resp = requests.get(url=url,headers=headers)
        print(resp.text)

    def test_05_get_site(self):
        url = "https://mg.kmelearning.com/system/manage/site/get?&companyCode=fulan&siteCode=fulan"
        token = ReadExtract().read_extract()['token']
        headers ={
            "Connection": "keep-alive",
            "Host": "mg.kmelearning.com",
            "Accept": "application/json,text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": Authorization
        }
        resp = requests.get(url=url,headers=headers)
        print(resp.text)


if __name__ == '__main__':
    pytest.main(['-vs'])
