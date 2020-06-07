#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-06-07 16:13:05
@Description:汉诺塔未完！
'''
i = 1
def move(n, mfrom, mto) :
  global i
  print("第%d步:将%d号盘子从%s -> %s" %(i, n, mfrom, mto))
  i += 1

def hanoi(n, A, B, C) :
  if n == 1 :
    move(1, A, C)         # 将第1个盘子从A移动到C
  else :
    hanoi(n - 1, A, C, B) # 将A上的前n-1个盘子借助C来移动到B上
    move(n, A, C)         # 将第n个盘子从A移动到C
    hanoi(n - 1, B, A, C) # 将B上的前n-1个盘子借助A来移动到C上

#********************程序入口**********************
if __name__ == "__main__":
  try :
    n = int(input("please input an integer :"))
    print("移动步骤如下：")
    hanoi(n, 'A', 'B', 'C')
  except ValueError:
    print("please input an integer n(n > 0)!" )
