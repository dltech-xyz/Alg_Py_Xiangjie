#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-06-07 21:20:42
@LastEditors: steven
@LastEditTime: 2020-06-07 22:20:25
@Description:
'''
if_reinput = input("是否重新输入，y表示是，n表示否:")
if if_reinput == 'y' or 'Y':
    need2pay = float(input("请输入需要找的零钱:"))
elif if_reinput == 'n' or 'N':
    return False
