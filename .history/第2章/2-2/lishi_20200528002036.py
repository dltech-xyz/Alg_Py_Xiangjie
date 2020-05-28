#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 00:20:35
@Description:将列表的最后几项作为历史记录的过程。
'''
import os

from _collections import deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)

    for line in lines:
        if pattern in line:
            yield line, previous_lines
            # #yield 生成器，暂时保存返回当前变量
        previous_lines.append(line)

# TODO：判断工作目录
# 修改工作目录
print (os.getcwd()) #打印出当前工作路径 D:\onedrive\文档\code\Python算法详解
# https://blog.csdn.net/JohinieLi/article/details/70855058
os.chdir('.\第2章\\2-2')
print (os.getcwd())

def f123():
        # with open('.\\123\.txt') as f: # FileNotFoundError: [Errno 2] No such file or directory: '.S.txt'
    # with open('.\\123.txt') as f: # FileNotFoundError: [Errno 2] No such file or directory: '.\\123.txt'
    # with open('\123.txt') as f: # FileNotFoundError: [Errno 2] No such file or directory: 'S.txt'
    # with open('123.txt') as f: # FileNotFoundError: [Errno 2] No such file or directory: '123.txt'
    with open('123.txt') as f:
        # ?
        for line, prevlines in search(f, 'python', 5):
            # #在此文件中搜索，规则是python ,次数是5次
            for pline in prevlines:
                print(pline)  # print (pline, end='')
            print(line)  # print (pline, end='')
        # ?
            print('-' * 20)

def SearchPython():
    with open('SearchPython.txt') as f:
        # ?
        for line, prevlines in search(f, 'python', 5):
            # #在此文件中搜索，规则是python ,次数是5次
            for pline in prevlines:
                print(pline)  # print (pline, end='')
            print(line)  # print (pline, end='')
        # ?
            print('-' * 20)

# Example use on a file
if __name__ == '__main__':
    # f123()
    SearchPython()

# 创造固定长度的队列,当队列满时,有新纪录,旧纪录自动移除.
q = deque(maxlen=3)

q.append(1)
q.append(2)
q.append(3)
print(q)

q.append(4)
print(q)

q.append(5)
print(q)
