#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 22:40:54
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
# del c['y'] # KeyError: "Key not found in the first mapping: 'y'"

#使用 update() 方法将两个字典合并,需要你创建一个完全不同的字典对象merged.
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = dict(b)
merged.update(a)

#破坏现有字典结构z，是后来加入的a里的。
print(merged['x'])  # 1
print(merged['y'])  # 2
print(merged['z'])  # 3

#  同时，如果原字典做了更新，这种改变不会反应到新的合并字典中去。
a['x'] = 13

print(merged['x'])  # 1
print(merged['y'])  # 2
print(merged['z'])  # 3

#ChainMap 使用原来的字典，它自己不创建新的字典。所以它并不会产生上面所说的结果
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = ChainMap(a, b)
merged['x'] #KeyError: 'x',因为已经del了
print(merged['x'])
a['x'] = 42
merged['x'] # Notice change to merged dicts
print(merged['x'])
