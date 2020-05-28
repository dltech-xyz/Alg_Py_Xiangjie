#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 00:33:27
@Description:通过内置heapq可实现简单的优先级队列.
'''

import heapq
# 利用
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        #列表的元素插入
        heapq.heappush(self._queue, (-priority, self._index, item))
        # (-priority, self._index, item) -priority取负值为了,从高到低的优先级排列.
        self._index += 1

    def pop(self):
        #列表的元素删除
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('AAA'), 1)
q.push(Item('BBB'), 4)
q.push(Item('CCC'), 5)
q.push(Item('DDD'), 1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

'''
Item('CCC')
Item('BBB')
Item('AAA')
Item('DDD')
'''
