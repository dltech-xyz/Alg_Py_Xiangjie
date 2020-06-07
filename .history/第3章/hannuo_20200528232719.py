#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 23:27:19
@Description:
'''
i = 1
def move(n, mfrom, mto) :
  global i
  print("第%d步:将%d号盘子从%s -> %s" %(i, n, mfrom, mto))
  i += 1

def hanoi(n, A, B, C) :
  if n == 1 :
    move(1, A, C)
  else :
    hanoi(n - 1, A, C, B)
    move(n, A, C)
    hanoi(n - 1, B, A, C)

#********************程序入口**********************
try :
  n = int(input("please input a integer :"))
  print("移动步骤如下：")
  hanoi(n, 'A', 'B', 'C')
except ValueError:
  print("please input a integer n(n > 0)!" )
