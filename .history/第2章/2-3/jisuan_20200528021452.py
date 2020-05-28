#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 02:14:52
@Description:
'''
price = {
    '小米': 899,
    '华为': 1999,
    '三星': 3999,
    '谷歌': 4999,
    '酷派': 599,
    'iPhone': 5000,
}

min_price = min(zip(price.values(), price.keys()))
# zip()可翻转字典的键和值.
# 将可迭代对象作为参数,将对象中对应的元素,打包成一个个的元组,然后返回有这些元组组成的列表.
# 如果各个迭代器的元素个数不一致,则返回的列表长度与最短对象的相同.
print(min_price)

max_price = max(zip(price.values(), price.keys()))
print(max_price)

#对字典中的数据排序sorted
price_sorted = sorted(zip(price.values(), price.keys()))

print(price_sorted)

price_and_names = zip(price.values(), price.keys())
print((min(price_and_names)))

# print (max(price_and_names))  error  zip()创建了迭代器，内容只能被消费一次
print(min(price))
print(max(price))
print(min(price.values()))
print(max(price.values()))
print(min(price, key=lambda k: price[k]))
print(max(price, key=lambda k: price[k]))
