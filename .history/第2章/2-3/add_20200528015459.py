#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 01:54:59
@Description:添加字典值
'''

dict = {'数学': '99', '语文': '99', '英语': '99' }  #创建字典“dict”
dict['物理'] ='100'        #添加字典值1 dict['物理'] =100 Incompatible types in assignment (expression has type "int", target has type "str")mypy(error)
dict['化学'] ='98'         #添加字典值2
print (dict)              #输出字典dict中的值
print ("物理成绩是：",dict['物理'])     #显示物理成绩
print ("化学成绩是：",dict['化学'])     #显示化学成绩
