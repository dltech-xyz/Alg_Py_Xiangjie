#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 01:45:29
@Description:清空有序字典中的数据.
'''
import collections

dic = collections.OrderedDict()
dic['k1'] = 'v1'
dic['k2'] = 'v2'
dic.clear()
print(dic)

#输出：OrderedDict()
