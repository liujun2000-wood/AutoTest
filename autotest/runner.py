# -*- coding: UTF-8 -*-
import os
from autotest.ddt.excel_ddt import ddt
if __name__ == '__main__':
    # os.system('rm -rf result')
    # os.system('rm -rf report')
    os.system('del result')
    os.system('del report')
    ddt.run_web_case('./lib/cases/mgcase.xlsx')
    os.system('allure generate result -o report --clean')


