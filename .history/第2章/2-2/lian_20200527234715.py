#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-27 23:47:15
@Description:元组可组合，不可修改
'''

tup1 = (12, 34.56);       	#定义元组tup1
tup2 = ('abc', 'xyz')       	#定义元组tup2
# 下面一行代码修改元组元素操作是非法的
# tup1[0] = 100
tup3 = tup1 + tup2;       	#创建一个新的元组tup3
print (tup3)             	#输出元组tup3中的值
