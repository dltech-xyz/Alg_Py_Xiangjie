#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-06-10 10:25:23
@Description:LILO队列
'''
from queue import Queue #LILO队列
# q = Queue() #创建队列对象
q: "Queue[int]" = Queue() #https://stackoverflow.com/questions/59689524/how-to-add-variable-type-annotation-for-what-goes-into-a-queue
q.put(0)    #在队列尾部插入元素
q.put(1)
q.put(2)
print('LILO队列',q.queue)  #查看队列中的所有元素
print(q.get())  #返回并删除队列头部元素
print(q.queue)

from queue import LifoQueue #LIFO队列
#lifoQueue = LifoQueue()
lifoQueue: "LifoQueue[int]" = LifoQueue()
lifoQueue.put(1)
lifoQueue.put(2)
lifoQueue.put(3)
print('LIFO队列',lifoQueue.queue)
lifoQueue.get() #返回并删除队列尾部元素
lifoQueue.get()
print(lifoQueue.queue)

from queue import PriorityQueue #优先队列
#priorityQueue = PriorityQueue() #创建优先队列对象
priorityQueue:"PriorityQueue[int]" = PriorityQueue()
priorityQueue.put(3)    #插入元素
priorityQueue.put(78)   #插入元素
priorityQueue.put(100)  #插入元素
print(priorityQueue.queue)  #查看优先级队列中的所有元素
priorityQueue.put(1)    #插入元素
priorityQueue.put(2)    #插入元素
print('优先级队列:',priorityQueue.queue)  #查看优先级队列中的所有元素
priorityQueue.get() #返回并删除优先级最低的元素
print('删除后剩余元素',priorityQueue.queue)
priorityQueue.get() #返回并删除优先级最低的元素
print('删除后剩余元素',priorityQueue.queue)  #删除后剩余元素
priorityQueue.get() #返回并删除优先级最低的元素
print('删除后剩余元素',priorityQueue.queue)  #删除后剩余元素
priorityQueue.get() #返回并删除优先级最低的元素
print('删除后剩余元素',priorityQueue.queue)  #删除后剩余元素
priorityQueue.get() #返回并删除优先级最低的元素
print('全部被删除后:',priorityQueue.queue)  #查看优先级队列中的所有元素

from collections import deque   #双端队列
dequeQueue:"deque[str]" = deque(['Eric','John','Smith'])
print(dequeQueue)
dequeQueue.append('Tom')    #在右侧插入新元素
dequeQueue.appendleft('Terry')  #在左侧插入新元素
print(dequeQueue)
dequeQueue.rotate(2)    #循环右移2次
print('循环右移2次后的队列',dequeQueue)
dequeQueue.popleft()    #返回并删除队列最左端元素
print('删除最左端元素后的队列：',dequeQueue)
dequeQueue.pop()    #返回并删除队列最右端元素
print('删除最右端元素后的队列：',dequeQueue)
