#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:21
@LastEditors: steven
@LastEditTime: 2020-05-27 23:42:24
@Description:切片slice
'''

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])

items[a] = [10, 11]
# 插入了，变成[0, 1, 10, 11, 4, 5, 6]
print(items)

print(a.start)
print(a.stop)
print(a.step)

s = 'HelloWorld'
print(a.indices(len(s)))
# 使用indices(size)函数将切片映射到指定大小的序列上，
# ? 将会返回一个(start,stop,step)元组，
# 所有的值都已经正好限制在边界以内，这样当进行索引操作时，
# ? 可以避免IndexError异常。
for i in range(*a.indices(len(s))):
    print(s[i])
