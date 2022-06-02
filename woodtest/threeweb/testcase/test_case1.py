# -*- coding: UTF-8 -*-
import re

import jsonpath
import pytest


class TestApi:

    @pytest.mark.parametrize('name,age', [['木木', '20'], ['木木一', '21'], ['木木二', '22']])
    def test_01_mumu(self, name, age):
        print(name, age)
        # 正则表达式提取
        result = re.search('"xxx":"(.*?)",',res.text)
        print(result.group(1))
        # json值提取,取到的值时list
        value = jsonpath.jsonpath(res.json(),"$.data")
        print(value[0])


if __name__ == '__main__':
    pytest.main()
