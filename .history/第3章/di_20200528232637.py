#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 23:26:37
@Description:
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
