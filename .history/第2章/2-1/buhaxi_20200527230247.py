#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:21
@LastEditors: steven
@LastEditTime: 2020-05-27 23:02:46
@Description:不可散列情况下，删除列表中重复的元素，并保持顺序不变
'''

def buha(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        # key 功能：将序列中的元素转换为可散列的类型，为了检测重复选项。
        # 处理数据，使之变成可以比较的格式，即把数据解构，其中key为解构函数，val为解构后的数据
        print(val)
        if val not in seen:
            yield item
            # 这里要塞入generator的是item，因为val只是为了方便处理生成的“中间数据”，并没有什么卵用
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
