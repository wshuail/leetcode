#
# @lc app=leetcode.cn id=82 lang=python
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (52.47%)
# Total Accepted:    148.5K
# Total Submissions: 283.1K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
# 
# 返回同样按升序排列的结果链表。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点数目在范围 [0, 300] 内
# -100 
# 题目数据保证链表已经按升序排列
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        dummy = ListNode(0, head)
        root = dummy
        while root.next and root.next.next:
            if root.next.val == root.next.next.val:
                x = root.next.val
                while root.next and root.next.val == x:
                    root.next = root.next.next
            else:
                root = root.next

        return dummy.next
