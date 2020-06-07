#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-06-07 22:46:58
@LastEditors: steven
@LastEditTime: 2020-06-07 22:46:59
@Description:
'''
#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-06-07 21:20:42
@LastEditors: steven
@LastEditTime: 2020-06-07 22:46:41
@Description:y/n,test
'''
if_reinput = input("是否重新输入，y表示是，n表示否:")
if if_reinput == "y" or if_reinput == "Y":
    # 不能省略or后面的if_reinput ==
    # if key == "name" and item: means if (key == "name") and (item evaluates to True).
    need2pay = float(input("请输入需要找的零钱:"))
elif if_reinput == "n" or if_reinput == "N":
    exit()
else :
    print(f"输入的{if_reinput}不是f也不是n，请重新输入")
# Python3.8:
# while res:= input("Do you want to save? (Enter y/n)").lower() not in {"y", "n"}: pass
# https://gist.github.com/garrettdreyfus/8153571
