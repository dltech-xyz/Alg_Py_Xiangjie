#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 22:45:20
@Description:
'''
nums = [1, 2, 3, 4, 5]
# s = sum((x * x for x in nums)) # 显式的传递一个生成器表达式对象
s = sum( x*x for x in nums ) # 使用一个生成器表达式作为参数，更加优雅的实现方式，省略了括号
# s = sum([x * x for x in nums]) # 会创建一个巨大的仅仅被使用一次就被丢弃的临时数据结构。而生成器方案会以迭代的方式转换数据，因此更省内存。
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
print(min_shares)
# Alternative: Returns {'name': 'AOL', 'shares': 20}
# min_shares = min(portfolio, key=lambda s: s['shares'])
