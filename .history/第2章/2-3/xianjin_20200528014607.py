#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 01:46:06
@Description:
'''

import collections

dic = collections.OrderedDict()
dic['k1'] = 'v1'
dic['k2'] = 'v2'
dic['k3'] = 'v3'
print(dic.popitem(),dic)
print(dic.popitem(),dic)

# ('k3', 'v3') OrderedDict([('k1', 'v1'), ('k2', 'v2')])
# ('k2', 'v2') OrderedDict([('k1', 'v1')])
