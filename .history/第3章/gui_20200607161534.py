#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-06-07 16:15:34
@Description:
'''
def fact(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * fact(n - 1)
        print("intermediate result for ", n, " * fact(", n - 1, "): ", res)
        return res


print(fact(10))
