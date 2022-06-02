# -*- coding: UTF-8 -*-
import unittest
from HTMLTestRunner import HTMLTestRunner

import pytest

if __name__ == '__main__':
    # 执行需要的用例，并生产html格式的自动化的测试报告
    # 使用unittest默认的测试用例加载器去发现testcase目录下py结尾的测试用例
    suite = unittest.defaultTestLoader.discover("./testcase", "*.py")
    unittest.main(defaultTest='suite')
    # 生产HTML报告文件
    report_file = open("./report/reports.html", "wb")
    # 生成一个HTMLTestRunner运行器对象（必须下载一个文件HTMLTestRunner.py,放到python的lib目录下）
    runner = HTMLTestRunner(stream=report_file, title="自动化测试报告", description="报告详情如下")
    # 通过运行器运行测试用例
    runner.run(suite)
    report_file.close()
