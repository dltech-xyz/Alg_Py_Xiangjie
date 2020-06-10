#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-06-08 10:59:16
@Description:贪心，计算最少的加油次数。参考：https://blog.csdn.net/jiyanfeng1/article/details/39361485
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
        if s >= n:   # 当局部和大于n时，那最后一段再跑就没有油了。
            num += 1 # 则在没到下一站前，将要加油。
            s = d[i] # 将局部和更新为d[n]，因为这一段之前没跑，加满油还要跑。
        i += 1
    print(num)

if __name__ == '__main__':
    greedy() # 贪心意在令每一次加满油之后跑尽可能多的距离
