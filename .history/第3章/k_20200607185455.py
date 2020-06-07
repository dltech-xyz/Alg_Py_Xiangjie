#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-06-07 18:54:49
@Description:用分治算法，找出序列中第K小的元素。
'''
# 划分（基于主元 pivot），注意：非就地划分
def partition(seq):
    pi = seq[0]  # 挑选主元
    lo = [x for x in seq[1:] if x <= pi]  # 所有小的元素
    hi = [x for x in seq[1:] if x > pi]  # 所有大的元素
    return lo, pi, hi

# 查找第 k+1 小的元素
def select(seq, k):
    # 分解
    lo, pi, hi = partition(seq)
    m = len(lo)
    if m == k:
        return pi  # 解决！
    elif m < k:
        return select(hi, k - m - 1)  # 递归（树），分治
    else:
        return select(lo, k)  # 递归（树），分治

if __name__ == '__main__':
    seq = [0, 1, 2]
    print(select(seq, 1))
