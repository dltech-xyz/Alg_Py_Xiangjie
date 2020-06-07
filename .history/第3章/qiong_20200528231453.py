#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 23:12:23
@Description:穷举，24点。造三种形式，其他可行的形式，都可转换为在加乘意义上这三种形式的表达式
#源代码：https://www.cnblogs.com/hhh5460/p/6926909.html
#TODO:还可扩展为GUI:https://python123.io/index/topics/homeworks/ershishiGUI
#TODO:https://www.nowcoder.com/questionTerminal/fbc417f314f745b1978fc751a54ac8cb?commentTags=Python
'''
import itertools


def twentyfour(cards):
    '''史上最短计算24点代码'''
    for nums in itertools.permutations(cards):  #? 四个数a,b,c,d随机？
        for ops in itertools.product('+-*/', repeat=3):  # 三个运算符（可重复！）
            # 构造三种中缀表达式 (bsd)
            bds1 = '({0}{4}{1}){5}({2}{6}{3})'.format(*nums, *ops)  # (a+b)*(c-d)
            bds2 = '(({0}{4}{1}){5}{2}){6}{3}'.format(*nums, *ops)  # (a+b)*c-d
            bds3 = '{0}{4}({1}{5}({2}{6}{3}))'.format(*nums, *ops)  # a/(b-(c/d))

            for bds in [bds1, bds2, bds3]:  # 遍历
                try:
                    if abs(eval(bds) - 24.0) < 1e-10:  # ? eval函数:可以将字符串转化成代码并执行
                        return bds
                except ZeroDivisionError:  # 零除错误！
                    continue

    return 'Not found!'



# 测试
# 数据来源：http://www.cnblogs.com/grenet/archive/2013/02/28/2936965.html
cards = [[1, 1, 1, 8],
         [1, 1, 2, 6],
         [1, 1, 2, 7],
         [1, 1, 2, 8],
         [1, 1, 2, 9],
         [1, 1, 2, 10],
         [1, 1, 3, 4],
         [1, 1, 3, 5],
         [1, 1, 3, 6],
         [1, 1, 3, 7],
         [1, 1, 3, 8],
         [1, 1, 3, 9],
         [1, 1, 3, 10],
         [1, 1, 4, 4],
         [1, 1, 4, 5],
         [1, 1, 4, 6],
         [1, 1, 4, 7],
         [1, 1, 4, 8],
         [1, 1, 4, 9],
         [1, 1, 4, 10],
         [1, 1, 5, 5],
         [1, 1, 5, 6],
         [1, 1, 5, 7],
         [1, 1, 5, 8],
         [1, 1, 6, 6],
         [1, 1, 6, 8],
         [1, 1, 6, 9],
         [1, 1, 7, 10],
         [1, 1, 8, 8],
         [1, 2, 2, 4],
         [1, 2, 2, 5],
         [1, 2, 2, 6],
         [1, 2, 2, 7],
         [1, 2, 2, 8],
         [1, 2, 2, 9],
         [1, 2, 2, 10],
         [1, 2, 3, 3],
         [1, 2, 3, 4],
         [1, 2, 3, 5],
         [1, 2, 3, 6],
         [1, 2, 3, 7],
         [1, 2, 3, 8],
         [1, 2, 3, 9],
         [1, 2, 3, 10],
         [1, 2, 4, 4],
         [1, 2, 4, 5],
         [1, 2, 4, 6],
         [1, 2, 4, 7],
         [1, 2, 4, 8],
         [1, 2, 4, 9],
         [1, 2, 4, 10],
         [1, 2, 5, 5],
         [1, 2, 5, 6],
         [1, 2, 5, 7],
         [1, 2, 5, 8],
         [1, 2, 5, 9],
         [1, 2, 5, 10],
         [1, 2, 6, 6],
         [1, 2, 6, 7],
         [1, 2, 6, 8],
         [1, 2, 6, 9],
         [1, 2, 6, 10],
         [1, 2, 7, 7],
         [1, 2, 7, 8],
         [1, 2, 7, 9],
         [1, 2, 7, 10],
         [1, 2, 8, 8],
         [1, 2, 8, 9],
         [1, 2, 8, 10],
         [1, 3, 3, 3],
         [1, 3, 3, 4],
         [1, 3, 3, 5],
         [1, 3, 3, 6],
         [1, 3, 3, 7],
         [1, 3, 3, 8],
         [1, 3, 3, 9],
         [1, 3, 3, 10],
         [1, 3, 4, 4],
         [1, 3, 4, 5],
         [1, 3, 4, 6],
         [1, 3, 4, 7],
         [1, 3, 4, 8],
         [1, 3, 4, 9],
         [1, 3, 4, 10],
         [1, 3, 5, 6],
         [1, 3, 5, 7],
         [1, 3, 5, 8],
         [1, 3, 5, 9],
         [1, 3, 5, 10],
         [1, 3, 6, 6],
         [1, 3, 6, 7],
         [1, 3, 6, 8],
         [1, 3, 6, 9],
         [1, 3, 6, 10],
         [1, 3, 7, 7],
         [1, 3, 7, 8],
         [1, 3, 7, 9],
         [1, 3, 7, 10],
         [1, 3, 8, 8],
         [1, 3, 8, 9],
         [1, 3, 8, 10],
         [1, 3, 9, 9],
         [1, 3, 9, 10],
         [1, 3, 10, 10],
         [1, 4, 4, 4],
         [1, 4, 4, 5],
         [1, 4, 4, 6],
         [1, 4, 4, 7],
         [1, 4, 4, 8],
         [1, 4, 4, 9],
         [1, 4, 4, 10],
         [1, 4, 5, 5],
         [1, 4, 5, 6],
         [1, 4, 5, 7],
         [1, 4, 5, 8],
         [1, 4, 5, 9],
         [1, 4, 5, 10],
         [1, 4, 6, 6],
         [1, 4, 6, 7],
         [1, 4, 6, 8],
         [1, 4, 6, 9],
         [1, 4, 6, 10],
         [1, 4, 7, 7],
         [1, 4, 7, 8],
         [1, 4, 7, 9],
         [1, 4, 8, 8],
         [1, 4, 8, 9],
         [1, 4, 9, 10],
         [1, 4, 10, 10],
         [1, 5, 5, 5],
         [1, 5, 5, 6],
         [1, 5, 5, 9],
         [1, 5, 5, 10],
         [1, 5, 6, 6],
         [1, 5, 6, 7],
         [1, 5, 6, 8],
         [1, 5, 6, 9],
         [1, 5, 6, 10],
         [1, 5, 7, 8],
         [1, 5, 7, 9],
         [1, 5, 7, 10],
         [1, 5, 8, 8],
         [1, 5, 8, 9],
         [1, 5, 8, 10],
         [1, 5, 9, 9],
         [1, 5, 9, 10],
         [1, 5, 10, 10],
         [1, 6, 6, 6],
         [1, 6, 6, 8],
         [1, 6, 6, 9],
         [1, 6, 6, 10],
         [1, 6, 7, 9],
         [1, 6, 7, 10],
         [1, 6, 8, 8],
         [1, 6, 8, 9],
         [1, 6, 8, 10],
         [1, 6, 9, 9],
         [1, 6, 9, 10],
         [1, 7, 7, 9],
         [1, 7, 7, 10],
         [1, 7, 8, 8],
         [1, 7, 8, 9],
         [1, 7, 8, 10],
         [1, 7, 9, 9],
         [1, 7, 9, 10],
         [1, 8, 8, 8],
         [1, 8, 8, 9],
         [1, 8, 8, 10],
         [2, 2, 2, 3],
         [2, 2, 2, 4],
         [2, 2, 2, 5],
         [2, 2, 2, 7],
         [2, 2, 2, 8],
         [2, 2, 2, 9],
         [2, 2, 2, 10],
         [2, 2, 3, 3],
         [2, 2, 3, 4],
         [2, 2, 3, 5],
         [2, 2, 3, 6],
         [2, 2, 3, 7],
         [2, 2, 3, 8],
         [2, 2, 3, 9],
         [2, 2, 3, 10],
         [2, 2, 4, 4],
         [2, 2, 4, 5],
         [2, 2, 4, 6],
         [2, 2, 4, 7],
         [2, 2, 4, 8],
         [2, 2, 4, 9],
         [2, 2, 4, 10],
         [2, 2, 5, 5],
         [2, 2, 5, 6],
         [2, 2, 5, 7],
         [2, 2, 5, 8],
         [2, 2, 5, 9],
         [2, 2, 5, 10],
         [2, 2, 6, 6],
         [2, 2, 6, 7],
         [2, 2, 6, 8],
         [2, 2, 6, 9],
         [2, 2, 6, 10],
         [2, 2, 7, 7],
         [2, 2, 7, 8],
         [2, 2, 7, 10],
         [2, 2, 8, 8],
         [2, 2, 8, 9],
         [2, 2, 8, 10],
         [2, 2, 9, 10],
         [2, 2, 10, 10],
         [2, 3, 3, 3],
         [2, 3, 3, 5],
         [2, 3, 3, 6],
         [2, 3, 3, 7],
         [2, 3, 3, 8],
         [2, 3, 3, 9],
         [2, 3, 3, 10],
         [2, 3, 4, 4],
         [2, 3, 4, 5],
         [2, 3, 4, 6],
         [2, 3, 4, 7],
         [2, 3, 4, 8],
         [2, 3, 4, 9],
         [2, 3, 4, 10],
         [2, 3, 5, 5],
         [2, 3, 5, 6],
         [2, 3, 5, 7],
         [2, 3, 5, 8],
         [2, 3, 5, 9],
         [2, 3, 5, 10],
         [2, 3, 6, 6],
         [2, 3, 6, 7],
         [2, 3, 6, 8],
         [2, 3, 6, 9],
         [2, 3, 6, 10],
         [2, 3, 7, 7],
         [2, 3, 7, 8],
         [2, 3, 7, 9],
         [2, 3, 7, 10],
         [2, 3, 8, 8],
         [2, 3, 8, 9],
         [2, 3, 8, 10],
         [2, 3, 9, 9],
         [2, 3, 9, 10],
         [2, 3, 10, 10],
         [2, 4, 4, 4],
         [2, 4, 4, 5],
         [2, 4, 4, 6],
         [2, 4, 4, 7],
         [2, 4, 4, 8],
         [2, 4, 4, 9],
         [2, 4, 4, 10],
         [2, 4, 5, 5],
         [2, 4, 5, 6],
         [2, 4, 5, 7],
         [2, 4, 5, 8],
         [2, 4, 5, 9],
         [2, 4, 5, 10],
         [2, 4, 6, 6],
         [2, 4, 6, 7],
         [2, 4, 6, 8],
         [2, 4, 6, 9],
         [2, 4, 6, 10],
         [2, 4, 7, 7],
         [2, 4, 7, 8],
         [2, 4, 7, 9],
         [2, 4, 7, 10],
         [2, 4, 8, 8],
         [2, 4, 8, 9],
         [2, 4, 8, 10],
         [2, 4, 9, 9],
         [2, 4, 9, 10],
         [2, 4, 10, 10],
         [2, 5, 5, 7],
         [2, 5, 5, 8],
         [2, 5, 5, 9],
         [2, 5, 5, 10],
         [2, 5, 6, 6],
         [2, 5, 6, 7],
         [2, 5, 6, 8],
         [2, 5, 6, 9],
         [2, 5, 6, 10],
         [2, 5, 7, 7],
         [2, 5, 7, 8],
         [2, 5, 7, 9],
         [2, 5, 7, 10],
         [2, 5, 8, 8],
         [2, 5, 8, 9],
         [2, 5, 8, 10],
         [2, 5, 9, 10],
         [2, 5, 10, 10],
         [2, 6, 6, 6],
         [2, 6, 6, 7],
         [2, 6, 6, 8],
         [2, 6, 6, 9],
         [2, 6, 6, 10],
         [2, 6, 7, 8],
         [2, 6, 7, 9],
         [2, 6, 7, 10],
         [2, 6, 8, 8],
         [2, 6, 8, 9],
         [2, 6, 8, 10],
         [2, 6, 9, 9],
         [2, 6, 9, 10],
         [2, 6, 10, 10],
         [2, 7, 7, 8],
         [2, 7, 7, 10],
         [2, 7, 8, 8],
         [2, 7, 8, 9],
         [2, 7, 9, 10],
         [2, 7, 10, 10],
         [2, 8, 8, 8],
         [2, 8, 8, 9],
         [2, 8, 8, 10],
         [2, 8, 9, 9],
         [2, 8, 9, 10],
         [2, 8, 10, 10],
         [2, 9, 10, 10],
         [3, 3, 3, 3],
         [3, 3, 3, 4],
         [3, 3, 3, 5],
         [3, 3, 3, 6],
         [3, 3, 3, 7],
         [3, 3, 3, 8],
         [3, 3, 3, 9],
         [3, 3, 3, 10],
         [3, 3, 4, 4],
         [3, 3, 4, 5],
         [3, 3, 4, 6],
         [3, 3, 4, 7],
         [3, 3, 4, 8],
         [3, 3, 4, 9],
         [3, 3, 5, 5],
         [3, 3, 5, 6],
         [3, 3, 5, 7],
         [3, 3, 5, 9],
         [3, 3, 5, 10],
         [3, 3, 6, 6],
         [3, 3, 6, 7],
         [3, 3, 6, 8],
         [3, 3, 6, 9],
         [3, 3, 6, 10],
         [3, 3, 7, 7],
         [3, 3, 7, 8],
         [3, 3, 7, 9],
         [3, 3, 8, 8],
         [3, 3, 8, 9],
         [3, 3, 8, 10],
         [3, 3, 9, 9],
         [3, 3, 9, 10],
         [3, 4, 4, 4],
         [3, 4, 4, 5],
         [3, 4, 4, 6],
         [3, 4, 4, 7],
         [3, 4, 4, 8],
         [3, 4, 4, 9],
         [3, 4, 4, 10],
         [3, 4, 5, 5],
         [3, 4, 5, 6],
         [3, 4, 5, 7],
         [3, 4, 5, 8],
         [3, 4, 5, 9],
         [3, 4, 5, 10],
         [3, 4, 6, 6],
         [3, 4, 6, 8],
         [3, 4, 6, 9],
         [3, 4, 6, 10],
         [3, 4, 7, 7],
         [3, 4, 7, 8],
         [3, 4, 7, 9],
         [3, 4, 7, 10],
         [3, 4, 8, 9],
         [3, 4, 8, 10],
         [3, 4, 9, 9],
         [3, 4, 10, 10],
         [3, 5, 5, 6],
         [3, 5, 5, 7],
         [3, 5, 5, 8],
         [3, 5, 5, 9],
         [3, 5, 6, 6],
         [3, 5, 6, 7],
         [3, 5, 6, 8],
         [3, 5, 6, 9],
         [3, 5, 6, 10],
         [3, 5, 7, 8],
         [3, 5, 7, 9],
         [3, 5, 7, 10],
         [3, 5, 8, 8],
         [3, 5, 8, 9],
         [3, 5, 9, 9],
         [3, 5, 9, 10],
         [3, 5, 10, 10],
         [3, 6, 6, 6],
         [3, 6, 6, 7],
         [3, 6, 6, 8],
         [3, 6, 6, 9],
         [3, 6, 6, 10],
         [3, 6, 7, 7],
         [3, 6, 7, 8],
         [3, 6, 7, 9],
         [3, 6, 7, 10],
         [3, 6, 8, 8],
         [3, 6, 8, 9],
         [3, 6, 8, 10],
         [3, 6, 9, 9],
         [3, 6, 9, 10],
         [3, 6, 10, 10],
         [3, 7, 7, 7],
         [3, 7, 7, 8],
         [3, 7, 7, 9],
         [3, 7, 7, 10],
         [3, 7, 8, 8],
         [3, 7, 8, 9],
         [3, 7, 9, 9],
         [3, 7, 9, 10],
         [3, 7, 10, 10],
         [3, 8, 8, 8],
         [3, 8, 8, 9],
         [3, 8, 8, 10],
         [3, 8, 9, 9],
         [3, 8, 9, 10],
         [3, 8, 10, 10],
         [3, 9, 9, 9],
         [3, 9, 9, 10],
         [3, 9, 10, 10],
         [4, 4, 4, 4],
         [4, 4, 4, 5],
         [4, 4, 4, 6],
         [4, 4, 4, 7],
         [4, 4, 4, 8],
         [4, 4, 4, 9],
         [4, 4, 4, 10],
         [4, 4, 5, 5],
         [4, 4, 5, 6],
         [4, 4, 5, 7],
         [4, 4, 5, 8],
         [4, 4, 5, 10],
         [4, 4, 6, 8],
         [4, 4, 6, 9],
         [4, 4, 6, 10],
         [4, 4, 7, 7],
         [4, 4, 7, 8],
         [4, 4, 7, 9],
         [4, 4, 7, 10],
         [4, 4, 8, 8],
         [4, 4, 8, 9],
         [4, 4, 8, 10],
         [4, 4, 10, 10],
         [4, 5, 5, 5],
         [4, 5, 5, 6],
         [4, 5, 5, 7],
         [4, 5, 5, 8],
         [4, 5, 5, 9],
         [4, 5, 5, 10],
         [4, 5, 6, 6],
         [4, 5, 6, 7],
         [4, 5, 6, 8],
         [4, 5, 6, 9],
         [4, 5, 6, 10],
         [4, 5, 7, 7],
         [4, 5, 7, 8],
         [4, 5, 7, 9],
         [4, 5, 7, 10],
         [4, 5, 8, 8],
         [4, 5, 8, 9],
         [4, 5, 8, 10],
         [4, 5, 9, 9],
         [4, 5, 9, 10],
         [4, 5, 10, 10],
         [4, 6, 6, 6],
         [4, 6, 6, 7],
         [4, 6, 6, 8],
         [4, 6, 6, 9],
         [4, 6, 6, 10],
         [4, 6, 7, 7],
         [4, 6, 7, 8],
         [4, 6, 7, 9],
         [4, 6, 7, 10],
         [4, 6, 8, 8],
         [4, 6, 8, 9],
         [4, 6, 8, 10],
         [4, 6, 9, 9],
         [4, 6, 9, 10],
         [4, 6, 10, 10],
         [4, 7, 7, 7],
         [4, 7, 7, 8],
         [4, 7, 8, 8],
         [4, 7, 8, 9],
         [4, 7, 8, 10],
         [4, 7, 9, 9],
         [4, 7, 9, 10],
         [4, 7, 10, 10],
         [4, 8, 8, 8],
         [4, 8, 8, 9],
         [4, 8, 8, 10],
         [4, 8, 9, 9],
         [4, 8, 9, 10],
         [4, 8, 10, 10],
         [4, 9, 9, 10],
         [5, 5, 5, 5],
         [5, 5, 5, 6],
         [5, 5, 5, 9],
         [5, 5, 6, 6],
         [5, 5, 6, 7],
         [5, 5, 6, 8],
         [5, 5, 7, 7],
         [5, 5, 7, 8],
         [5, 5, 7, 10],
         [5, 5, 8, 8],
         [5, 5, 8, 9],
         [5, 5, 8, 10],
         [5, 5, 9, 9],
         [5, 5, 9, 10],
         [5, 5, 10, 10],
         [5, 6, 6, 6],
         [5, 6, 6, 7],
         [5, 6, 6, 8],
         [5, 6, 6, 9],
         [5, 6, 6, 10],
         [5, 6, 7, 7],
         [5, 6, 7, 8],
         [5, 6, 7, 9],
         [5, 6, 8, 8],
         [5, 6, 8, 9],
         [5, 6, 8, 10],
         [5, 6, 9, 9],
         [5, 6, 9, 10],
         [5, 6, 10, 10],
         [5, 7, 7, 9],
         [5, 7, 7, 10],
         [5, 7, 8, 8],
         [5, 7, 8, 9],
         [5, 7, 8, 10],
         [5, 7, 9, 10],
         [5, 7, 10, 10],
         [5, 8, 8, 8],
         [5, 8, 8, 9],
         [5, 8, 8, 10],
         [5, 9, 10, 10],
         [6, 6, 6, 6],
         [6, 6, 6, 8],
         [6, 6, 6, 9],
         [6, 6, 6, 10],
         [6, 6, 7, 9],
         [6, 6, 7, 10],
         [6, 6, 8, 8],
         [6, 6, 8, 9],
         [6, 6, 8, 10],
         [6, 6, 9, 10],
         [6, 7, 7, 10],
         [6, 7, 8, 9],
         [6, 7, 8, 10],
         [6, 7, 9, 9],
         [6, 7, 10, 10],
         [6, 8, 8, 8],
         [6, 8, 8, 9],
         [6, 8, 8, 10],
         [6, 8, 9, 9],
         [6, 8, 9, 10],
         [6, 9, 9, 10],
         [6, 10, 10, 10],
         [7, 7, 9, 10],
         [7, 8, 8, 9],
         [7, 8, 8, 10],
         [7, 8, 9, 10],
         [7, 8, 10, 10],
         [8, 8, 8, 10]]

for card in cards:
    print(twentyfour(card))
