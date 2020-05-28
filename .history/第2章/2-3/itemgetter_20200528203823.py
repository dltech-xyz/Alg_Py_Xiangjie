#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-28 20:24:55
@LastEditors: steven
@LastEditTime: 2020-05-28 20:38:23
@Description:https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p13_sort_list_of_dicts_by_key.html?highlight=itemgetter
'''
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

if __name__ == "__main__":
    from operator import itemgetter
    rows_by_fname = sorted(rows, key=itemgetter('fname')) #从小到大。
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    print(rows_by_fname)
    print('\n')
    print(rows_by_uid)
    print('\n') # 右下
    # print(rows_by_uid+'/n') #TypeError: can only concatenate list (not "str") to list
    # 优先lname 的a-z,当都是Jones，比Big<Brian.
    rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))

    print(rows_by_lfname)
