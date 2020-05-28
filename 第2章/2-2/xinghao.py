#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-27 23:57:19
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

'''
*args 和 **kwargs 主要用于函数定义。 你可以将不定数量的参数传递给一个函数。
这里的不定的意思是：预先并不知道, 函数使用者会传递多少个参数给你, 所以在这个场景下使用这两个关键字。 *args 是用来发送一个非键值对的可变数量的参数列表给一个函数.
https://wiki.jikexueyuan.com/project/interpy-zh/args_kwargs/Usage_args.html
'''
