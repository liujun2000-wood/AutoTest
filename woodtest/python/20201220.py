# -*- coding: utf-8 -*- 
# @Time : 2020/12/20 22:16 
# @Author : Aries 
# @Site :  
# @File : 20201220.py 
# @Software: PyCharm
# liujun
"""
abs()函数----获取绝对值
abs(x)
"""
tupleAbs = [12.45,0,-19.34]
# for num in tupleAbs:
#     print(abs(num))

#定义函数,用于输出2个数字相乘后的绝对值

def calcAbs(value1,value2):
    return abs(value1*value2)
# print(calcAbs(12.96,8.2))
# print(calcAbs(10,-10))

"""
divmod()函数----获取商和余数的元组,返回一个包含商和余数的元组(a//b,a%b).
divmod(a,b)
"""
def getdivmod(A,N):
    while N>0:
        sn =str(N)
        sa =str(A)
        result = ['divmod({0},{1}):'.format(sn,sa),str(divmod(N,A))]
        print(''.join(result))
        N = N-1
# getdivmod(3,10)

# 模拟实现数据分页计算方法

def getsegment(curindex,getsize):
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    startget = (curindex - 1)*getsize
    getdata = abc[startget:curindex*getsize]
    totalindextuple = divmod(len(abc),getsize)
    totalindex = totalindextuple[0]+(1 if totalindextuple[1] > 0 else 0)
    return (getdata,totalindex)
result = getsegment(2,7)
# print(result)

