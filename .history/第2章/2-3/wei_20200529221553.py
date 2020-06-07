#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-29 22:15:53
@Description:itemgetter（）可获取对象中指定域的值，参数为一些序数。
'''
from operator import itemgetter
a = [1,2,3]
b=itemgetter(1)      #定义函数b，获取对象的第1个域的值
print(b(a))

b=itemgetter(1,0)  #定义函数b，获取对象的第1个域和第0个的值
print(b(a))
