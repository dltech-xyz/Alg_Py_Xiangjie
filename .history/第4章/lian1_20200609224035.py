#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-06-08 19:10:11
@Description:https://zhuanlan.zhihu.com/p/47100824
'''

class Node(object):
    # 在python 3 中已经默认就帮你加载了object了（即便你没有写上object）。https://my.oschina.net/zhengtong0898/blog/636468
    def __init__(self, data, pnext = None):
        """
        data:节点保存的数据
        _next:保存下一个节点对象
        """
        self.data = data
        self._next = pnext

    def __repr__(self):
        """
        用于定义Node的字符输出，
        ?print用于输出data
        """
        return str(self.data)

class ChainTable(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return (self.length == 0)

    # 增加一个节点(在链表尾添加): append()
    def append(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, Node):# item令为节点类的实例
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1

        else:
            # 移动到已有的最后节点。
            node = self.head
            while node._next:
                node = node._next
            # 链接上新节点
            node._next = item
            self.length += 1

    # 增加一个节点(在链表头添加): add()
    def add(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode   # 节点类的实例
        else:
            item = Node(dataOrNode)  # 节点类的实例

        if not self.head:
            self.head = item
            self.length += 1

        else:
            nextnode = self.head
            self.head = item
            item._next = nextnode
            self.length += 1

    # 删除一个节点:delete()
    def delete(self, index):
        if self.isEmpty():
            print("this chain table is empty.")
            return

        if index < 0 or index >= self.length:
            print('error: out of index')
            return

        # 要注意删除第一个节点的情况
        # ?如果有空的头节点就不用这样
        # 但是我不喜欢弄头节点
        # 区别就是return
        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        # prev为保存前导节点
        # node为保存当前节点
        # 当j与index相等时就相当于找到要删除的节点
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next # node不断向后移动
            j += 1

        if j == index:
            prev._next = node._next # 将前导节点的指针令为删除节点的指针，即指向要删除节点后的节点。
            self.length -= 1        # 减少长度。

    # 插入一个节点: insert()
    def insert(self, index, dataOrNode):
        if self.isEmpty():
            print("this chain table is empty")
            return

        if index < 0 or index >= self.length:
            print("error: out of index")
            return

        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return

        j = 0
        node = self.head
        prev = self.head
        #
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

    # 修改一个节点：update()
    def update(self, index, data):
        if self.isEmpty() or index < 0 or index >= self.length:
            print('error: out of index')
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        if j == index:
            node.data = data

    # 查找一个节点: getItem()
    def getItem(self, index):
        if self.isEmpty() or index < 0 or index >= self.length:
            print("error: out of index")
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        return node.data

    # 查找一个节点的索引: getIndex()
    def getIndex(self, data):
        j = 0
        if self.isEmpty():
            print("this chain table is empty")
            return
        node = self.head
        while node:
            if node.data == data:
                return j
            node = node._next
            j += 1

        if j == self.length:
            print("%s not found" % str(data))
            return

    def clear(self):
        self.__init__()

    def __repr__(self):
        if self.isEmpty():
            return("empty chain table")
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.data) + ' '
            node = node._next
        return nlist

    # ?区别 https://stackoverflow.com/questions/12447036/why-getitem-cannot-be-classmethod
    def __getitem__(self, ind):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print("error: out of index")
            return
        return self.getItem(ind)

    def __setitem__(self, ind, val):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print("error: out of index")
            return
        self.update(ind, val)

    def __len__(self):
        return self.length