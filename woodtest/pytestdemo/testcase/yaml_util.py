# -*- coding: UTF-8 -*-
import yaml


class YamlUtil:
    def __init__(self, yaml_file):
        """
        通过init方法把yaml文件传入到这个类
        :param yaml_file:
        """
        self.yaml_file = yaml_file
    # 读取yaml文件
    def read_yaml(self):
        """
        读取yaml，对yaml反序列化，就是把我们的yaml格式换成dict格式.
        :return:
        """
        with open(self.yaml_file, encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            # print(value, type(value))
            return value


if __name__ == '__main__':
    YamlUtil('test_api.yaml').read_yaml()