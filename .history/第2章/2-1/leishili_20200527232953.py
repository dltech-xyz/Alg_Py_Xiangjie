#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:21
@LastEditors: steven
@LastEditTime: 2020-05-27 23:29:53
@Description:
'''

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

# 原来的顺序
users = [User(19), User(17), User(18)]
print(users)

# 根据user_id排序
print(sorted(users, key=lambda u: u.user_id))
from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))

