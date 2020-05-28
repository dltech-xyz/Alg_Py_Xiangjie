#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 00:39:28
@Description:
'''
import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

a = Item('AAA')
b = Item('BBB')
#a < b
a = (1, Item('AAA'))
b = (5, Item('BBB'))
print(a < b)
c = (1, Item('CCC'))
#a < c
a = (1, 0, Item('AAA'))
b = (5, 1, Item('BBB'))
c = (1, 2, Item('CCC'))
print(a < b)
print(a < c)
