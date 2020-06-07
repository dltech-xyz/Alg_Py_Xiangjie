#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-06-07 22:59:49
@Description:最少的零钱数给顾客。
'''
# 检验一个输入数是否为正整数：#https://www.quora.com/How-can-I-make-sure-the-user-inputs-a-positive-integer-in-Python
def pos_num(n,i):
    face_value = [0.01,0.02,0.05,0.1,0.2,0.5,1.0]
    while type(n) is not int:
        try:
            # n = input("Please enter a positive integer: ")
            num = int(n)
            if num < 0:
                print(f"{face_value[i]}:{n} is not positive.\n")
                pos_num()
            return num
        except ValueError:
            print(f"{face_value[i]}:{n} is not positive.\n")

def check_money(need2pay,all_money):
    test_100need2pay = need2pay*100
    if test_100need2pay.is_integer():# TODO:溢出怎么办？
    # .is_integer(): https://www.zhihu.com/question/51078882/answer/124089031
    # 遇到超出浮点数精度范围的问题，一样会出现错误：
        try:
            if need2pay > all_money:
                # 当输入的总金额比收银员的总金额多时，无法进行找零
                print("付不起，请检查输入的钱是否有误。\n")

                if_reinput = input("是否重新输入，y表示是，n表示否:")
                #y/n,非法字符检验:
                if if_reinput == "y" or if_reinput == "Y":
                    # 不能省略or后面的if_reinput ==
                    # if key == "name" and item: means if (key == "name") and (item evaluates to True).
                    need2pay = float(input("请输入需要找的零钱:"))
                elif if_reinput == "n" or if_reinput == "N":
                    print("将退出")
                    exit()
                else :
                    print(f"输入的{if_reinput}不是f也不是n，请重新输入")
                return 0 # ?https://stackoverflow.com/questions/12348697/why-would-a-function-end-with-return-0-instead-of-return-in-python
        except ValueError:
            print(f"输入的{need2pay}不是数字，请重新输入")
    else :
        print(f"{need2pay} 该输入不正确.\n")

def main():
    # 初始化钱数为0和储存各面值的硬币的列表：
    face_value = [0.01,0.02,0.05,0.1,0.2,0.5,1.0] # 存储每种硬币面值
    fval_num = [] # 存储每种硬币的数量
    all_money = 0 # 总钱数（初始）为0

    # 输入现在拥有的零钱：
    temp = input("请按【1分，2分，5分，1角，2角，5角，1元】的顺序，来输入每种零钱的数量，用空格来分割：")
    fval_num0 = temp.split(" ")

    # 检验输入的序列是否为正整数：
    for item in fval_num0: # x in mylist is better and more readable than x in mylist[:]
        pos_num(fval_num0(item),item)

    # 拥有的零钱总和
    for i in range(0, len(fval_num0)):
        fval_num.append(int(fval_num0[i]))
        all_money += face_value[i] * fval_num[i] # 计算出收银员总共拥有多少钱

    need2pay = float(input("请输入需要找的零钱:"))
    check_money(need2pay,all_money)  #检查这有没超过还剩的钱。
    all_money = all_money - need2pay #更新还剩下的钱。

    # 要想用的钱币数量最少，那么需要利用所有面值大的钱币，因此从数组的面值大的元素开始遍历
    i = len(face_value)-1
    while i >= 0:
        if need2pay >= face_value[i]:
            n = int(need2pay / face_value[i])
            if n > fval_num[i]:
                n = fval_num[i]  # 最多用已有的硬币数，来支付。
            fval_num[i] -= n     # 更新硬币数。
            need2pay -= n * face_value[i] # 贪心的关键步骤，令sum动态的改变，
            print(f'用了{n}个{face_value[i]}元硬币')
        i -= 1

if __name__ == "__main__":
    main()
