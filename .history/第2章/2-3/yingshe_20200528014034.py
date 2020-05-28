#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 01:40:34
@Description:一键多值字典[multidict]
'''
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

from collections import defaultdict
# defaultdict能自动初始化第一个值.

#第一种方式:为字典中的键创建相同的多值键.
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
print(d)

#第二种方式:为字典中的键创建相同的多值键.
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(3)
print(d)

# defaultdict()会自动创建字典表项,以待稍后访问,不想该功能,在普通字典上setdefault()
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(3)
print(d)

#第一种方式:为字典中的初始化第一个值.
d = {}
for key, value in d:  # pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
d = defaultdict(list)
print(d)

#第二种方式:为字典中的初始化第一个值.
for key, value in d:  # pairs:
    d[key].append(value)
print(d)
