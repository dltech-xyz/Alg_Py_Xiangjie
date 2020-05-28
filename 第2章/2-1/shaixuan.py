#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:21
@LastEditors: steven
@LastEditTime: 2020-05-27 23:33:32
@Description:列表推导式的筛选
'''

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# All positive values
zheng = [n for n in mylist if n > 0]
print(zheng)

# All negative values
fu = [n for n in mylist if n < 0]
print(fu)
