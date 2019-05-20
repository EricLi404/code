# coding=utf-8
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    抄的。。这方法妙啊
    """
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode is None:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]
