#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 20:22:05
@Description:
'''
from operator import itemgetter
a = [1,2,3]
b=itemgetter(1)      #定义函数b，获取对象的第1个域的值
print(b(a))

b=itemgetter(1,0)  #定义函数b，获取对象的第1个域和第0个的值
print(b(a))
