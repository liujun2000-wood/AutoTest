# -*- coding: UTF-8 -*-


import yaml


class ReadExtract:
    def __init__(self):
        self.yaml_path = 'extract.yaml'

    # 读取, dict of list
    def read_extract(self):
        with open(self.yaml_path, mode='r', encoding='utf-8') as f:
            # Loader=yaml.FullLoader 加载的方式
            yaml_data = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
            return yaml_data

    # 写入
    def write_extract(self, data):
        # mode='a' 追加的方式
        with open(self.yaml_path, mode='w', encoding='utf-8') as f:
            # data = [{'name': '接口用例的名称', 'request': {'method': 'get', 'url': 'https://mg.kmelearning.com/web-manage/manage/course/chapter/list', 'data': {'courseId': 1519921311010230272, 'companyCode': 'fulan', 'siteCode': 'fulan'}}, 'validate': [{'equals': {'status_code': 200}}, {'contains': '没有令牌信息,请重新登陆'}]}]
            # 内容有中文是需要加：allow_unicode=True，避免写入unicode
            yaml.dump(data, stream=f, allow_unicode=True)
    # 写入
    def write_extract(self, data):
        # mode='a' 追加的方式
        with open(self.yaml_path, mode='w', encoding='utf-8') as f:
            # data = [{'name': '接口用例的名称', 'request': {'method': 'get', 'url': 'https://mg.kmelearning.com/web-manage/manage/course/chapter/list', 'data': {'courseId': 1519921311010230272, 'companyCode': 'fulan', 'siteCode': 'fulan'}}, 'validate': [{'equals': {'status_code': 200}}, {'contains': '没有令牌信息,请重新登陆'}]}]
            # 内容有中文是需要加：allow_unicode=True，避免写入unicode
            yaml.dump(data, stream=f, allow_unicode=True)