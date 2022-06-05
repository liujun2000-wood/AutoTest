# -*- coding: UTF-8 -*-
import os
import pytest
from autotest.common.excle import get_reader, get_writer
from autotest.common.logger import logger
from playwright.sync_api import sync_playwright

class DDT:
    def __init__(self):
        """初始化一些实例变量"""
        play = sync_playwright().start()
        brower = play.chromium.launch(headless=False)
        page = brower.new_page()

        self.web = page

        # 记录项目模块,分组名字
        self.feature = ''
        self.story = ''

        # 记录重命名的序号
        self.story_idx = 0
        # 记录项目模块的序号
        self.feature_idx = 0

        # 记录一个模块的用例
        self.cases = []
        # 记录运行的类型
        self.type = 'web'

        # 写入excel结果
        self.writer = None

    def __run_pytest_case(self):
        logger.info(str(self.story_idx))
        # 通过更改文件名,去运行数据驱动
        os.rename('./ddt/test_%s_%d.py' % (self.type, self.story_idx - 1,),
                  './ddt/test_%s_%d.py' % (self.type, self.story_idx,))

        pytest.main(['-s', './ddt/test_%s_%d.py' % (self.type, self.story_idx,), '--alluredir', 'result'])

    def run_web_case(self, filepath='./lib/cases/mgcase.xlsx'):
        self.type = 'web'
        print(filepath)
        reader = get_reader(filepath)
        sheetname = reader.get_sheets()
        logger.info(sheetname)
        for sheet in sheetname:
            # 设置当前读取的sheet页面
            reader.set_sheet(sheet)
            # 设置项目模块名字
            self.feature = sheet
            self.feature_idx += 1
            lines = reader.readline()

            case= []
            # 表头不需要
            for i in range(1,len(lines)):
                line = lines[i]
                # 第一个单元格有内容,说明是一个新的模块
                if len(line[0]) > 0:
                    # 如果模块用例不为空,说明上一个模块已经完成
                    # 需要吧上一个用例添加到cases里面去,并且执行整个用例
                    if case:
                        self.cases.append(case)
                        logger.debug(self.cases)
                        logger.debug('执行用例')
                        self.__run_pytest_case()

                    self.cases = []
                    case =[]
                    # 记录模块名称
                    self.story = line[0]
                    logger.debug(line)
                    self.story_idx +=1
                # 第二个单元格有内容,说明是用例
                elif len(line[1])> 0:
                    # 如果case不为空,说明上一组用例统计完成
                    # 把用例放到模块用例cases里面去
                    if case:
                        self.cases.append(case)

                    # 用一个列表准备存放一组测试用例的所有数据
                    case =[]
                    case.append(line)
                else:
                    # 记录一组用例的数据
                    case.append(line)

            # 1个sheet统计完成,吧最后一个用例添加到模块里面
            # 并且执行最后一个sheet
            if case:
                self.cases.append(case)
                logger.debug(self.cases)
                logger.debug('执行用例')
                self.__run_pytest_case()

            # 主要置空,否则每一个sheet最后一个分组可能多次执行
            self.cases = []
            case = []

        # 所有用例跑完后,把文件名还原
        os.rename('./ddt/test_web_%d.py' % (self.story_idx,), './ddt/test_web_0.py')


ddt = DDT()




