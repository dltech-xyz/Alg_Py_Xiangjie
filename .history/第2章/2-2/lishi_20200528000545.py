#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 00:05:45
@Description:将列表的最后几项作为历史记录的过程。
'''

from _collections import deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)

    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

import os

print os.getcwd() #打印出当前工作路径
# Example use on a file
if __name__ == '__main__':
    # with open('.\\123\.txt') as f: # FileNotFoundError: [Errno 2] No such file or directory: '.S.txt'
    # with open('.\\123.txt') as f: # FileNotFoundError: [Errno 2] No such file or directory: '.\\123.txt'
    # with open('\123.txt') as f: # FileNotFoundError: [Errno 2] No such file or directory: 'S.txt'
    with open('123.txt') as f: # FileNotFoundError: [Errno 2] No such file or directory: '123.txt'

        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline)  # print (pline, end='')
            print(line)  # print (pline, end='')
            print('-' * 20)
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
