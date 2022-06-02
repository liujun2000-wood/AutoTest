# -*- coding: UTF-8 -*-
import unittest

import jsonpath
import requests
from ddt import file_data,ddt

@ddt
class MgCase(unittest.TestCase):

    @file_data('test.yaml')
    def test01_get_token(self,  **kwargs):
        print(kwargs)
        # print(kwargs['request']['mothod'])
        # print(kwargs['request']['data'])
        # print(kwargs['validate'])
        if 'name' in kwargs.keys() and 'request' in kwargs.keys() and 'validate' in kwargs.keys():
            if jsonpath.jsonpath(kwargs, '$..url') and jsonpath.jsonpath(kwargs, '$..method'):
                res = requests.get(url=kwargs['request']['url'], params=kwargs['request']['data'])
                print(res.json(), type(res.json()))
                # print(kwargs['validate'])
                for assert_type in kwargs['validate']:
                    for key, value in dict(assert_type).items():
                        if key == 'equals':
                            pass
                        elif key == "contains":
                            if value in res.text:
                                print('断言通过')
                            else:
                                print('断言失败')
            else:
                print('request目录下必须有url和method')
        else:
            print('一级关键字必须包含：name，request，validate')




if __name__ == '__main__':
    unittest.main()