#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:56:16
@LastEditors: steven
@LastEditTime: 2020-05-27 22:56:44
@Description:https://zhuanlan.zhihu.com/p/35067086
'''
L = [3, 8, 1, 2, 3, 3, 4, 5, 4, 5, 6, 7, 8]

for i in L:
    if L.count(i) >= 2:
        L.remove(i)
print(L)
# [1, 2, 3, 4, 5, 6, 7, 8]


for i in L:
    if L.count(i) >= 2:
        L.pop(i)
print(L)
# [3, 8, 1, 3, 5, 4, 6, 7]

L1 = set(L)
print(L1)
# {1, 2, 3, 4, 5, 6, 7, 8}
