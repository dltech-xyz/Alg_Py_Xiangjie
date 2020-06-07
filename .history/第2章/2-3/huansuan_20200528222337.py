#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 22:23:37
@Description:
'''
nums = [1, 2, 3, 4, 5]
s = sum( x*x for x in nums )
print(s)
import os
os.chdir('.\第2章\\2-3') #我加的
files = os.listdir('.idea')
if any(name.endswith('.py') for name in files):
    print('这是一个Python文件!')
else:
    print('这里没有Python文件!')
s = ('RMB', 50, 128.88)
print(','.join(str(x) for x in s))

portfolio = [
    {'name': 'AAA', 'shares': 50},
    {'name': 'BBB', 'shares': 65},
    {'name': 'CCC', 'shares': 40},
    {'name': 'DDD', 'shares': 35}
]

min_shares = min(s['shares'] for s in portfolio)
