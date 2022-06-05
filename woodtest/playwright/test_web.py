# -*- coding: UTF-8 -*-

# 读取用例
import allure
import pytest
import yaml
from playwright.sync_api import sync_playwright

f = open('testcase.yaml', mode='r')
cases_dict = yaml.safe_load(f)
# print(cases_dict)


@allure.feature('报告标题')
class Test_web:

    def run_step(self, func, value):
        """
        显示每一步执行了什么关键字以及具体的参数是什么
        :param func:
        :param value:
        :return:
        """
        func(*value)

    def run_case(self, POCases):
        allure.dynamic.title(POCases['title'])
        allure.dynamic.description(POCases['des'])
        # 获取所有测试用例
        cases = POCases['cases']
        try:
            for case in cases:
                func = self.page.__getattribute__(case['method'])
                # 获取参数
                caselist = list(case.values())
                with allure.step(case['name']):
                    self.run_step(func, caselist[2:])
        except Exception:
            allure.attach(self.page.screenshot(),'用例报错图',allure.attachment_type.PNG)
            pytest.fail('用例执行失败')
        allure.attach(self.page.screenshot(),'用例执行图',allure.attachment_type.PNG )

    def setup_class(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(channel="chrome", headless=False)
        self.page = self.browser.new_page()

    @allure.story('登录')
    @pytest.mark.parametrize('POCcases', cases_dict['loginpage'])
    def test_login(self, POCcases):
        self.run_case(POCcases)
        self.page.wait_for_timeout(2000)

    def teardown_class(self):
        self.page.wait_for_timeout(1000)
        self.browser.close()
        self.playwright.stop()