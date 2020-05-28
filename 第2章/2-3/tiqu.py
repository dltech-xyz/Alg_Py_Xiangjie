#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 21:08:34
@Description:创造一个字典的子集，前两个快，查看更多：https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p17_extract_subset_of_dict.html
'''
prices = {'ASP.NET': 49.9, 'Python': 69.9, 'Java': 59.9, 'C语言': 45.9, 'PHP': 79.9}
p1 = {key: value for key, value in prices.items() if value > 50}
print(p1)
tech_names = {'Python', 'Java', 'C语言'}

p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)

p3 = dict((key, value) for key, value in prices.items() if value > 50)  # 慢
print(p3)

tech_names = {'Python', 'Java', 'C语言'}
p4 = {key: prices[key] for key in prices.keys() if key in tech_names}  # 慢
print(p4)
