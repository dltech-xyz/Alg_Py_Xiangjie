#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-06-08 10:55:26
@Description:贪心，计算最少的加油次数。
'''
def greedy():
    # 初始化
    n = 100 # 油箱里的加满油时的油量能走的距离。
    d = [50,80,39,60,40,32]     # 表示各个加油站之间的距离
    k = len(d)-1 # 计算出加油站数-1，用以循环计算。
    # 先检测
    for i in range(k):  # 先检测各加油站之间的距离，
        if d[i] > n:    # 若发现其中有一个距离大于汽车加满油能跑的距离，
            print('no solution') # 则输出no solution。
            return
    # 加油
    i, s = 0, 0
    # 利用s进行迭代
    num = 0    # 表示加油次数
    while i <= k:
        s += d[i]
        if s >= n:   # 当局部和大于n时，
            num += 1 # 则在没到下一站前，将要加油。
            s -= d[i]    # 将局部和更新为0，方便下次计算。
        i += 1
    print(num)

if __name__ == '__main__':
    greedy() # 贪心意在令每一次加满油之后跑尽可能多的距离
