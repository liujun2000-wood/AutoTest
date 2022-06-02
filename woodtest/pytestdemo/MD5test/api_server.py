# -*- coding: UTF-8 -*-
import json
import requests
import hashlib
from urllib3.util import request
# pip install flask
from flask import Flask

app = Flask(__name__)

# 自定义接口：post请求，data传参
@app.route('/get_token', method=["post"])
def login():
    username = requests.getParameter("username")
    password = requests.getParameter("password")
    print(requests.heads)
    print(username, password)

    if username ==str(hashlib.md5('admin')).upper() and password ==str(hashlib.md5('123')).upper():
        return {'error_code': '1000', 'message': '登录成功', 'data': [{'api_token': hashlib.md5('admin123')}]}
    else:
        return {'error_code': '4000', 'message': '登录失败', 'data': []}

# 自定义接口：post请求，json
@app.route('/get_tokens', method=["post"])
def logins():
    print(requests.headers)
    data = json.loads(requests.get_data())
    print(data)
    if data['username'] == str(hashlib.md5('admin')).upper() and data['password'] == str(hashlib.md5('123')).upper():
        return {'error_code': '1000', 'message': '登录成功', 'data': [{'api_token': hashlib.md5('admin123')}]}
    else:
        return {'error_code': '4000', 'message': '登录失败', 'data': []}


if __name__ == '__main__':
    app.run()