#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-06-07 12:39:16
@Description:求斐波那契数列的第n项
'''
fib_table = {}  # memoization table to store previous terms

def fib_num(n):
    if (n <= 1):
        return n
    if n not in fib_table:
        fib_table[n] = fib_num(n - 1) + fib_num(n - 2)
    return fib_table[n]

n = int(input("输入斐波那契数列的第n项 \n"))
print("斐波那契数数列的第 ", n, "项是", fib_num(n))

# 用字典保存斐波那契数列，空间复杂度n
# 因为暴力递归，其时间复杂度为O(2^N).
# TODO:从左到右依次求出每一项的值，那么通过顺序计算求得第N项即可。其时间复杂度为O(N)。
# TODO:用矩阵乘法的形式表示，切状态矩阵为2*2的矩阵。将时间复杂度降至O(logN)
# https://blog.csdn.net/u012684062/article/details/76330075
