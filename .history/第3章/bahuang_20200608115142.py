#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-06-08 11:51:41
@Description:回溯法，八皇后
'''
n = 8
x = []  # 一个解（n元数组）
X = []  # 一组解


# 冲突检测：判断 x[k] 是否与前 x[0~k-1] 冲突
def conflict(k):
    global x

    for i in range(k):  # 遍历前 x[0~k-1]
        if x[i] == x[k] or abs(x[i] - x[k]) == abs(i - k):  # 判断是否与 x[k] 冲突
            return True
    return False


# 套用子集树模板
def queens(k):  # 到达第k行
    global n, x, X

    if k >= n:  # 超出最底行
        # print(x)
        X.append(x[:])  # 保存（一个解），注意x[:]
    else:
        for i in range(n):  # 遍历第 0~n-1 列（即n个状态）
            x.append(i)  # 皇后置于第i列，入栈
            if not conflict(k):  # 剪枝，排除掉冲突的。
                queens(k + 1)
            x.pop()  # 回溯，出栈


# 解的可视化（根据一个解x，复原棋盘。'X'表示皇后）
def show(x):
    global n

    for i in range(n):
        print('. ' * (x[i]) + 'X ' + '. ' * (n - x[i] - 1))
    print('\n')

if __name__ == "__main__":
    # 测试
    queens(0)  # 从第0行开始

    # 打印最后一个解
    print(X[-1], '\n')
    show(X[-1])

    # 筛选出右上角有皇后的情况：
    #print([x[0] for x in X]) #用列表解析的方法读取一列 https://blog.csdn.net/songyunli1111/article/details/78109976
    # TODO:https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p16_filter_sequence_elements.html
    col = [x[0] for x in X] #读取X里x的第一个元素，即X的列元素。
    # print(col.index(7)) # https://www.programiz.com/python-programming/methods/list/index
    col_v7=[index for index, value in enumerate(col) if value == 7] # enumerate:https://www.geeksforgeeks.org/enumerate-in-python/
    # print()
    # if [x[0] for x in X] == 7 :
    #     print(X[x], '\n')
    for row in col_v7:
        print(X[row], '\n')
        show(X[row])
