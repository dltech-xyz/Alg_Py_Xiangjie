#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:21
@LastEditors: steven
@LastEditTime: 2020-05-27 22:32:34
@Description:删除列表中重复的元素，并保持顺序不变
'''
# 实现了可散列情况下的删除重复元素功能，并保持顺序不变
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            # ?:
            yield item
            seen.add(item)
            # ?.

if __name__ == '__main__':
    a = [5, 5, 2, 1, 9, 1, 5, 10]
    print(a)
    print(list(dedupe(a)))
