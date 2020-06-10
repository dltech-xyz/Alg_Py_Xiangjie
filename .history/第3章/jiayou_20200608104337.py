#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-06-08 10:43:37
@Description:贪心，计算最少的加油次数。
'''
def greedy():
    n = 100 # 油箱里的加满油时的油量能走的距离。
    d = [50,80,39,60,40,32]     # 表示各个加油站之间的距离
    k = len(d)-1 # 计算出加油站数-1，用以循环计算。

    for i in range(k):  # 先检测各加油站之间的距离，
        if d[i] > n:    # 若发现其中有一个距离大于汽车加满油能跑的距离，
            print('no solution') # 则输出no solution。
            return

    i, s = 0, 0
    # 利用s进行迭代
    num = 0
    # 表示加油次数
    while i <= k:
        s += d[i]
        if s >= n:
            # 当局部和大于n时则局部和更新为当前距离
            s = d[i]
            # 贪心意在令每一次加满油之后跑尽可能多的距离
            num += 1
        i += 1
    print(num)

if __name__ == '__main__':
    greedy()
