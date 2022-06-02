# -*- coding: utf-8 -*- 
# @Time : 2020/11/29 22:38 
# @Author : Aries 
# @Site :  
# @File : python4.py 
# @Software: PyCharm
# liujun

#遍历文件夹目录os.walk()
# 1.os.walk() 方法用于通过在目录树种游走输出在目录中的文件名，向上或者向下。
#
# 2.walk()方法语法格式如下：
#
# os.walk(top，topdown=True，onerror=None， followlinks=False)
#
# top 根目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】。
#
# topdown 可选，为True或者没有指定, 一个目录的的3-元组将比它的任何子文件夹的3-元组先产生 (目录自上而下)。如果topdown为 False, 一个目录的3-元组将比它的任何子文件夹的3-元组后产生 (目录自下而上)。
#
# onerror 可选，是一个函数; 它调用时有一个参数, 一个OSError实例。报告这错误后，继续walk,或者抛出exception终止walk。
#
# followlinks 设置为 true，则通过软链接访问目录。
import os
path = r"D:\work\python\woodtest"
for fpath,dirname,fnames in os.walk(path):
    print(fpath)
    print(dirname)
    print(fnames)
def get_files(path='d:\\xx',rule=".py"):
    all = []
    for fpathe,dirs,fs in os.walk(path):
        for f in fs:
            filename = os.path.join(fpathe,f)
            if filename.endswith(rule):
                all.append(filename)
    return all

if __name__ =="__main__":
    b = get_files(r"D:\work\python\woodtest")
    for i in b:
        print(i)
