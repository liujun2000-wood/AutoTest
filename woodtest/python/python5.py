# -*- coding: utf-8 -*- 
# @Time : 2020/11/30 21:00 
# @Author : Aries 
# @Site :  
# @File : python5.py 
# @Software: PyCharm
# liujun


import csv,codecs
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
f = codecs.open("xieru.csv",'w+',"gbk")
writer = csv.writer(f)
data = ["客户名称","行业类型","客户联系人","职位","联系方式","邮箱","地址"]
writer.writerow(data)
datas = [
    ["客户名称", "行业类型", "客户联系人", "职位", "联系方式", "邮箱","地址"],
    ["客户名称", "行业类型", "客户联系人", "职位", "联系方式", "邮箱","地址"],
    ["客户名称", "行业类型", "客户联系人", "职位", "联系方式", "邮箱","地址"],
       ]

writer.writerows(datas)

f.close()