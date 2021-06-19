#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (41.76%)
# Total Accepted:    173.6K
# Total Submissions: 415.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 500] 内
# -100 
# 0 
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head

        length = 0
        root = head
        while root is not None:
            length += 1
            root = root.next

        if k%length == 0:
            return head

        k = k%length

        length -= k
        dummy = ListNode
        dummy.next = head
        root = dummy
        while length > 0:
            length -= 1
            root = root.next

        tail = root.next
        root.next = None

        root = tail
        while root is not None and root.next is not None:
            root = root.next
        root.next = dummy.next

        return tail
        
            




