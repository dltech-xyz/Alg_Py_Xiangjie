#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 22:16:47
@Description:
'''
rows = [
    {'address': '5412 N CLARK', 'data': '07/01/2018'},
    {'address': '5232 N CLARK', 'data': '07/04/2018'},
    {'address': '5542 E 58ARK', 'data': '07/02/2018'},
    {'address': '5152 N CLARK', 'data': '07/03/2018'},
    {'address': '7412 N CLARK', 'data': '07/02/2018'},
    {'address': '6789 w CLARK', 'data': '07/03/2018'},
    {'address': '9008 N CLARK', 'data': '07/01/2018'},
    {'address': '2227 W CLARK', 'data': '07/04/2018'}
]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

from collections import defaultdict

rows_by_date = defaultdict(list)

for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/04/2018']:
    print(r)
