#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Easy (75.09%)
# Total Accepted:    382.7K
# Total Submissions: 507K
# Testcase Example:  '[1,null,2,3]'
#
# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,2,3]
# 输出：[3,2,1]
# 
# 
# 示例 2：
# 
# 
# 输入：root = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目在范围 [0, 100] 内
# -100 <= Node.val <= 100
# 
# 
# 
# 
# 进阶：递归算法很简单，你可以通过迭代算法完成吗？
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return self.res

        if root.left:
            self.postorderTraversal(root.left)
        if root.right:
            self.postorderTraversal(root.right)

        self.res.append(root.val)

        return self.res
