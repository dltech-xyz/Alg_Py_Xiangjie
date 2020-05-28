#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-27 23:55:37
@Description:*表达式分解可迭代对象。
'''
records = [
    ('AAA', 1, 2),
    ('BBB', 'hello'),
    ('CCC', 5, 3)
]


def do_foo(x, y):
    print('AAA', x, y)

def do_bar(s):
    print('BBB', s)

for tag, *args in records:
    if tag == 'AAA':
        do_foo(*args)
    elif tag == 'BBB':
        do_bar(*args)

line = 'guan:ijing234://wef:678d:guan'
uname, *fields, homedir, sh = line.split(':')
print(uname)
# print(*fields) # ijing234 //wef
print(homedir)
