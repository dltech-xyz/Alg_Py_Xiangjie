#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:21
@LastEditors: steven
@LastEditTime: 2020-05-27 23:31:02
@Description:
'''

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares1 = [x**2 for x in range(10)]
print(squares1)
