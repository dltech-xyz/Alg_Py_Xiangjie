#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:21
@LastEditors: steven
@LastEditTime: 2020-05-27 23:34:11
@Description:
'''



values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
 try:
       x = int(val)
       return True
 except ValueError:
       return False
ivals = list(filter(is_int, values))
print(ivals)
