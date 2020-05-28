#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 20:50:49
@Description:
'''

from operator import itemgetter
rows = [
    {'fname': 'AAA', 'lname': 'ZHANG', 'uid': 1001},
    {'fname': 'BBB', 'lname': 'ZHOU', 'uid': 1002},
    {'fname': 'CCC', 'lname': 'WU', 'uid': 1004},
    {'fname': 'DDD', 'lname': 'LI', 'uid': 1003}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print('\n')
print(rows_by_uid)
print('\n')

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)
print('\n')

# lambda parameter_list: expression 可实现相似功能，但itemgetter()更快。
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['fname'], r['lname']))
print(rows_by_fname)
print('\n')
print(rows_by_lfname)
print('\n')

print(min(rows, key=itemgetter('uid')))
print('\n')
print(max(rows, key=itemgetter('uid')))
print('\n')
