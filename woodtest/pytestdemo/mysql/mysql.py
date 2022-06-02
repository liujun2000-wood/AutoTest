# -*- coding: UTF-8 -*-

import pymysql


conn = pymysql.connect(
    host="127.0.0.1",
    user='root',
    password='123456',
    database='exam')
cursor = conn.cursor()
cursor.execute("select version();")
# 获取内容
res = cursor.fetchall()
print(res)