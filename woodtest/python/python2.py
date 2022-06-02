# -*- coding: utf-8 -*- 
# @Time : 2020/11/29 18:54 
# @Author : Aries 
# @Site :  
# @File : python2.py 
# @Software: PyCharm
# liujun

#冒泡排序

li = [1, 3, 10, 9, 21, 35, 4, 6]
# for i in range(len(li)-1):
#     for j in range(len(li)-1-i):
#         if li[j]>li[j+1]:
#             li[j],li[j+1]=li[j+1],li[j]
#             # print(li)
# print(li)

s = range(len(li))[::-1]
print(list(s))
for i in s:
    for j in range(i):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
            print(i,j)
print(li)