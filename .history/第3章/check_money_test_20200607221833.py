#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-06-07 21:31:45
@LastEditors: steven
@LastEditTime: 2020-06-07 22:17:48
@Description:
'''
need2pay = float(2.111)
all_money = float(1)
"""
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
 """
def check_money(need2pay,all_money):
    test_100need2pay = need2pay*100
    if test_100need2pay.is_integer():# TODO:溢出怎么办？
    # .is_integer(): https://www.zhihu.com/question/51078882/answer/124089031
    # 遇到超出浮点数精度范围的问题，一样会出现错误：
        try:
            if need2pay > all_money:
                # 当输入的总金额比收银员的总金额多时，无法进行找零
                print("付不起，请检查输入的钱是否有误。\n")

                try:
                    # 选择重新输入钱
                    if_reinput = input("是否重新输入，y表示是，n表示否:")
                    if if_reinput == 'y' or 'Y':
                        # 检验再次的输入。
                        need2pay = float(input("请输入需要找的零钱:"))
                        check_money(need2pay,all_money)
                    else if_reinput == 'n' or 'N':
                        print("您已经退出本次交易。")
                        exit()
                except ValueError:
                        print(f"输入的{need2pay}不是f也不是n，请重新输入")
                    return 0 # ?https://stackoverflow.com/questions/12348697/why-would-a-function-end-with-return-0-instead-of-return-in-python
        except ValueError:
            print(f"输入的{need2pay}不是数字，请重新输入")
    else :
        print(f"{need2pay} 该输入不正确.\n")

check_money(need2pay,all_money)
