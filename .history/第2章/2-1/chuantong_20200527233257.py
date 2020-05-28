#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:21
@LastEditors: steven
@LastEditTime: 2020-05-27 23:32:53
@Description:List Comprehension列表推导式 variable = [out_exp_res for out_exp in input_list if out_exp ==2 ]
'''

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# List Comprehension:
squares1 = [x**2 for x in range(10)]
print(squares1)
