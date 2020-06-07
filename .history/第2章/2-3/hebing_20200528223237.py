#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 22:32:37
@Description:合并多个字典或映射 https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p20_combine_multiple_map_to_single_map.html
'''
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

#假设你必须在两个字典中执行查找操作（比如先从 a 中找，如果找不到再在 b 中找）。
from collections import ChainMap
c = ChainMap(a,b)

print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)
print(len(c))
print(list(c.keys()))
print(list(c.values()))

c['z'] = 10
c['w'] = 40
del c['x']
print(a)
del c['y'] # KeyError: "Key not found in the first mapping: 'y'"
