#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# https://leetcode-cn.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (56.44%)
# Total Accepted:    76.6K
# Total Submissions: 134.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 计算给定二叉树的所有左叶子之和。
# 
# 示例：
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
# 
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        if root.left and root.left.left is None and root.left.right is None:
            res += root.left.val

        res += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

        return res

    """
        return self.helper(root, False)

    def helper(self, root, flag):
        if not root:
            return 0
        if not root.left and not root.right and flag:
            return root.val
        return self.helper(root.left, True) + self.helper(root.right, False)
    """
