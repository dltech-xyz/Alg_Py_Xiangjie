#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 20:21:49
@Description:a.items() & b.items()寻找并获取两个字典中相同的键值对。
'''

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'x': 11,
    'y': 2,
    'w': 10
}
print(a.keys() & b.keys())  # {'x','y'}
print(a.keys() - b.keys())  # {'z'}
print(a.items() & b.items())  # {('y', 2)}

#字典推导式，可修改或过滤字典中的内容。
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)  # {'x':1, 'y':2}
