#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-06-08 12:04:39
@Description:
'''
def insert_list(L, i, element):
    L_length = len(L)
    if i < 1 or i > L_length:
        return False
    if i <= L_length:
        for k in range(i-1, L_length)[::-1]:
            L[k+1:k+2] = [L[k]]
        L[i-1] = element
    print(L)
    return True
L = [1,2,3,4]
insert_list(L, 2, 0)
