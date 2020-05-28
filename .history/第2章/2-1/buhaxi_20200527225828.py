#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:21
@LastEditors: steven
@LastEditTime: 2020-05-27 22:58:27
@Description:不可散列情况下，删除列表中重复的元素，并保持顺序不变
'''

def buha(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        # key 功能：将序列中的元素转换为可散列的类型，为了检测重复选项。
        if val not in seen:
            yield item
            seen.add(val)

if __name__ == '__main__':
    a = [
        {'x': 2, 'y': 3},
        {'x': 1, 'y': 4},
        {'x': 2, 'y': 3},
        {'x': 2, 'y': 3},
        {'x': 10, 'y': 15}
        ]
    print(a)
    print(list(buha(a, key=lambda a: (a['x'],a['y']))))
    #匿名函数（即“解构函数”）以x,y为主键 https://www.jianshu.com/p/290017656cd5
