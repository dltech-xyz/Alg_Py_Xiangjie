#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-06-07 17:02:19
@Description:分治算法，判断某元素是否再列表里
'''
# 子问题算法（子问题规模为 1）
def is_in_list(init_list, el):
    return [False, True][init_list[0] == el]
    # 不过在Python3.x 中，终于把这个两变量变成了关键字，而不再是内建（built-in）变量（在Python2.7）。
    # 也就是说，程序员再也没法给这两变量赋新的值了，从此True永远指向真对象，False指向假对象
    # https://foofish.net/python-true-false.html

# 分治法
def solve(init_list, el):
    n = len(init_list)
    if n == 1:  # 若问题规模等于 1，直接解决
        return is_in_list(init_list, el)

    # 分解（子问题规模为 n/2）
    left_list, right_list = init_list[:n // 2], init_list[n // 2:]

    # 递归（树），分治，合并(此处为深度优先,注意逻辑短路)
    # 短路逻辑：如果a为true，那么跳过b的判断，直接true
    # 也就是从前到后。set是无序,tuple和list有序。
    res = solve(left_list, el) or solve(right_list, el)

    return res


if __name__ == "__main__":
    # 测试数据
    test_list = [12, 2, 23, 45, 67, 3, 2, 4, 45, 63, 24, 23]
    # 查找
    print(solve(test_list, 45))  # True
    print(solve(test_list, 5))  # False
