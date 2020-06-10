#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-06-10 10:03:38
@Description:
'''


#异常类
class stringTypeError(TypeError):
    pass

#节点类
class Node(object):
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_
#单链表类
class single_list(object):
    def __init__(self):
        self._head = None
        self._num  = 0

    def __len__(self): # 这个是所有元素数-1
        return self._num

    def prepend(self,elem):
        self._head = Node(elem, self._head)
        self._num += 1

    def append(self,elem):
        if self._head is None:
            self._head = Node(elem)
            self._num += 1
            return
        p = self._head
        while p.next:
            p = p.next
        p.next = Node(elem)
        self._num += 1

    def pop_last(self):
        if self._head is None:
            raise ValueError("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            self._num -= 1
            return e
        while p.next.next:
            p = p.next
        e = p.next.elem
        p.next = None
        self._num -= 1
        return e

    def delitem(self, key):
        if key == len(self)-1:
            self.pop_last()
        elif 0<= key < len(self) - 1:
            p = self._head
            pre = None
            num = -1
            while p is not None:
                num += 1
                if key==num:
                    if not pre:
                        self._head = p.next
                        self._num -= 1
                    else:
                        pre.next = p.next
                        self._num -= 1
                    break
                else:
                    pre = p
                    p = p.next
        else:
            raise IndexError

    def insert(self, key, elem):
        if key>=len(self)-1:
            self.append(elem)
        elif 0<=key<len(self)-1:
            p = self._head
            pre = None
            num = -1
            while p:
                num += 1
                if num==key:
                    if not pre:
                        self._head = Node(elem, self._head)
                        self._num += 1
                    else:
                        pre.next = Node(elem, pre.next)
                        self._num += 1
                    break
                else:
                    pre = p
                    p = p.next
        else:
            raise IndexError

    # 打印显示
    def printall(self):
        p = self._head
        while p:
            print(p.elem, end="")
            if p.next:
                print(", ", end="")
            p = p.next
        print("")


#单链表字符串类
class string(single_list):
    def __init__(self, value):
        self.value = str(value)
        single_list.__init__(self)
        for i in range(len(self.value)-1,-1,-1):
            self.prepend(self.value[i])

    def length(self):
        return self._num

    def printall(self):
        p = self._head
        print("字符串结构：",end="")
        while p:
            print(p.elem, end="")
            if p.next:
                print("-->", end="")
            p = p.next
        print("")

    #朴素的串匹配算法，返回匹配的起始位置
    # 暴力匹配算法 https://blog.csdn.net/v_july_v/article/details/7041827
    # int ViolentMatch(char* s, char* p)
    def naive_matching(self, p):  #self为目标字符串，p为要查找的字符串(模式串)
        if not isinstance(self, string) and not isinstance(p, string):
            raise stringTypeError

        i, j = 0, 0                      #i表示self匹配到的位置，j表示p匹配到的位置
        m, n = self.length(), p.length() # m,n = len(p),len(self) https://blog.csdn.net/weixin_40539952/article/details/104280148

        while i < m and j < n:
            if p.value[i] == self.value[j]:#字符相同，匹配成功，考虑下一对字符
                i, j = i+1, j+1
            else:               #字符不同，考虑p中下一个位置
                i, j = i-j+1, 0 #当匹配中途中断时需要回到上一个位置的下一个位置
        if j == n:              #j==n 说明找到匹配,返回其下标
            return i-j
        return -1

    # kmp匹配算法，返回匹配的第一个位置,若没有匹配上返回-1
    # https://blog.csdn.net/your_answer/article/details/79619406
    # if s==len(son_string):return j-i;是因为i=1开始的。
    #? TODO:https://blog.csdn.net/v_july_v/article/details/7041827
    # 文本串的长度为m,匹配过程的时间复杂度为O(m),再加上计算pnext的O(n)时间，KMP的整体时间复杂度为O(m + n)。
    def matching_KMP(self, p):  # self母串，p字串。
        if not isinstance(self, string) and not isinstance(p, string):
            raise stringTypeError

        i, j = 0, 0                     # i表示self匹配到的位置，j表示p匹配到的位置
        m, n = self.length(), p.length() # 这个后面不用len-1,区别于m,n = len(p),len(self) https://blog.csdn.net/weixin_40539952/article/details/104280148

        while i < m and j < n:
            if j == -1 or self.value[i] == p.value[j]:
                i, j = i+1, j+1
            else:
                j = string.gen_next(p)[j]# j所对应的next值
        if j == n:                      # j==n说明找到匹配,返回其下标
            return i-j
        return -1




    # 生成pnext表
    @staticmethod
    #  A static method does not receive an implicit first argument.
    # 不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样
    # 如果在@staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。
    # https://www.jianshu.com/p/a95e0ade3445
    # 优化过后的next 数组求法：https://blog.csdn.net/v_july_v/article/details/7041827
    # 模式串的长度为n,计算pnext的O(n)时间
    def gen_next(p):
        j, k, n = 0, -1, p.length() # 因为后面令pnext[j] = k，k实际上就是pnext[j]

        pnext = [-1] * n # 主要目的是让第一个元素为-1，可参考： next[0] = -1 next 数组考虑的是除当前字符外的最长相同前缀后缀，所以通过第①步骤求得各个前缀后缀的公共元素的最大长度后，只要稍作变形即可
        while j < n - 1:                                   # 因为j一直在增加，k == -1不可能是子串只有一个元素，那样的话，就退出while，所以这表示又从子串的开始匹配了。
            if k == -1 or p.value[j] == p.value[k]:        # p.value[k] 表示前缀最后的元素， p.value[j]表示后缀最后的元素。
                j, k = j + 1, k + 1     # 新的元素匹配上了，k（即前缀后缀公共元素的最大长度）+1。并移动j向后指代。
                if p.value[j] != p.value[k]:# 黄《红黄》时：https://img-blog.csdn.net/20150812214857858
                    pnext[j] = k        # pnext[j] = k 代表p.value[j] 之前的模式串子串中，有长度为k 的相同前缀和后缀。
                else:                   # 因为p.value[j]已经跟s.value[i]失配，然后你还用跟p.value[j]等同的值p.value[next[j]]去跟s[i]匹配，很显然，必然失配.
                    pnext[j] = pnext[k] # 因为不能出现p.value[j] = p.value[pnext[j]]，所以当出现时需要继续递归，k = pnext[k] = pnext[pnext[k]]
            else:
                k = pnext[k] # 相当于模式串的自我匹配，所以不断的递归：让模式串右移k - pnext[k] 位，# 使得模式串的前缀p0 p1, ..., pk-1对应着文本串 si-k si-k+1, ..., si-1，而后让pk 跟si 继续匹配。
        return pnext         # j == n-1了，移动到最后，表示匹配完毕。

    # 因为python字符串对象为不变对象，所以replace方法并不修改原先的字符串，而是返回修改后的字符串。
    # 把old字符串出现的位置换成new字符串
    def replace(self, old, new):
        if not isinstance(self, string) and not isinstance(old, string) \
                and not isinstance(new, string):
            raise stringTypeError

        #删除匹配的旧字符串
        start = self.matching_KMP(old)
        for i in range(old.length()):
            self.delitem(start)
        #末尾情况下时append追加的，顺序为正；而前面的地方插入为前插；所以要分情况
        # append与insert的区别，前者p.next不存在！后者存在！
        if start<self.length():
            for i in range(new.length()-1, -1, -1):
                self.insert(start,new.value[i])
        else:
            for i in range(new.length()): #
                # self.insert(start,new.value[i])
                self.append(start,new.value[i])

if __name__=="__main__":

    a = string("abcda")
    print("字符串长度：",a.length())
    a.printall()
    b = string("abcabaabcdabdabcda")
    print("字符串长度：", b.length())
    b.printall()
    print("朴素算法_匹配的起始位置：",b.naive_matching(a),end=" ")
    print("KMP算法_匹配的起始位置：",b.matching_KMP(a))
    c = string("xu")
    print("==")
    b.replace(a,c)
    print("替换后的字符串是：")
    b.printall()
