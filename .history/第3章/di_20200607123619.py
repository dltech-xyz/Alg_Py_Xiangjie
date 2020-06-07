#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-06-07 12:36:19
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
# 因为暴力递归，其时间复杂度为O(2^N).https://blog.csdn.net/u012684062/article/details/76330075


