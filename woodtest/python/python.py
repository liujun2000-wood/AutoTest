# -*- coding: utf-8 -*-
# @Time : 2020/11/30 22:20 
# @Author : Aries 
# @Site :  
# @File : python.py 
# @Software: PyCharm
# liujun
# 1、从键盘输入整数n（1-9之间），对于1-100之间的整数删除包括n并且能被n整除的数，例如如何n为6，
# 则要删除包含6的如6,16这样的数及时6的倍数如12、18这样的数，输出所有满足条件的数，
# 要求每满10个数换行。
# 如：输入6
# 输入数字:6
# 结果：
# 1,2,3,4,5,7,8,9,10,11
# 13,14,15,17,19,20,21,22,23,25
# 27,28,29,31,32,33,34,35,37,38
# 39,40,41,43,44,45,47,49,50,51
# 52,53,55,57,58,59,70,71,73,74
# 75,77,79,80,81,82,83,85,87,88
# 89,91,92,93,94,95,97,98,99,100
"""
n = int(input("请输入一个数字："))
# count = 0
# new_str = ''
a = []
print("结果：")
for i in range(101):
    s = str(i)
    if i % n !=0 and s.find(str(n)) ==-1:
        a.append(i)
# print(a)
for i in range(1,len(a)+1):
    print(a[i-1],end=' ')
    if  i %10 ==0:
        print()
"""
# 随机函数产生500行1-100之间的随机整数存入文件random.txt中，
# 编程寻找这些整数的众数并输出。
import random
with open('radom.txt','w+') as fp:
    for i in range(500):
        fp.write(str(random.randint(1,100)))
        fp.write('\n')
        fp.seek(0)
        nums=fp.readlines()
nums=[num.strip()for num in nums]
setNums = set(nums)
print(setNums)
lst =[0]*101
for num in setNums:
    c = nums.count(num)
    print(c)
    lst[int(num)] =c
    print(lst)
for i in range(len(lst)):
    if lst[i] == max(lst):
        print(i)