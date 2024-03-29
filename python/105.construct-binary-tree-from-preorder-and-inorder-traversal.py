#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (70.48%)
# Total Accepted:    255.3K
# Total Submissions: 362.2K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 给定一棵树的前序遍历 preorder 与中序遍历  inorder。请构造二叉树并返回其根节点。
# 
# 
# 
# 示例 1:
# 
# 
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# 
# 
# 示例 2:
# 
# 
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 
# inorder.length == preorder.length
# -3000 
# preorder 和 inorder 均无重复元素
# inorder 均出现在 preorder
# preorder 保证为二叉树的前序遍历序列
# inorder 保证为二叉树的中序遍历序列
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.hash_table = {num: i for i, num in enumerate(inorder)}
        return self.helper(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)

    def helper(self, preorder, inorder, l_start, l_end, r_start, r_end):
        if r_start > r_end:
            return None
        root = TreeNode()
        root.val = preorder[l_start]
        if l_start == l_end:
            return root

        mid_idx = self.hash_table[preorder[l_start]]
        root.left = self.helper(preorder, inorder, l_start+1, l_start+1+mid_idx-1-r_start, r_start, mid_idx-1)
        root.right = self.helper(preorder, inorder, l_start+1+mid_idx-r_start, l_end, mid_idx+1, r_end)

        return root



