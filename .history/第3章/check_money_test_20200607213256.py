#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-06-07 21:31:45
@LastEditors: steven
@LastEditTime: 2020-06-07 21:32:55
@Description:
'''
need2pay = 1
all_money = 2
def check_money(need2pay,all_money):
    while type(need2pay) is not float:
        try:
            if need2pay > all_money:
                # 当输入的总金额比收银员的总金额多时，无法进行找零
                print("付不起，请检查输入的钱是否有误。\n")
                # 选择重新输入钱
                if_reinput = input("是否重新输入，y表示是，n表示否:")
                if if_reinput == 'y' or 'Y':
                    # TODO:检验再次的输入。
                    need2pay = float(input("请输入需要找的零钱:"))
                    check_money(need2pay,all_money)
                elif if_reinput == 'n' or 'N':
                    exit()
                    # TODO:非法字符检验。。
                return 0 # ?
        except ValueError:
            print(f"输入的{need2pay}不是数字，请重新输入")
