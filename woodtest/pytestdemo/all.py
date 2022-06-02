# -*- coding: UTF-8 -*-
import os

import pytest



if __name__ == '__main__':
    #1.生成临时的json文件
    pytest.main(['--alluredir','./temps','--clean-alluredir'])
    # 2.通过临时的json生成allure报告
    os.system('allure generate ./temps -o ./reports --clean')