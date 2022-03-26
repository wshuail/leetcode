#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#
# https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (51.35%)
# Total Accepted:    88K
# Total Submissions: 167.1K
# Testcase Example:  '[1,null,2,2]'
#
# 给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。
# 
# 如果树中有不止一个众数，可以按 任意顺序 返回。
# 
# 假定 BST 满足如下定义：
# 
# 
# 结点左子树中所含节点的值 小于等于 当前节点的值
# 结点右子树中所含节点的值 大于等于 当前节点的值
# 左子树和右子树都是二叉搜索树
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,2,2]
# 输出：[2]
# 
# 
# 示例 2：
# 
# 
# 输入：root = [0]
# 输出：[0]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目在范围 [1, 10^4] 内
# -10^5 <= Node.val <= 10^5
# 
# 
# 
# 
# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
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
        self.hash = {}
        self.res = []
        self.max_count = 0
    
    def findMode(self, root: TreeNode) -> List[int]:
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            return 
        
        self.dfs(root.left)
        
        if root.val not in self.hash:
            self.hash[root.val] = 1
        else:
            self.hash[root.val] += 1
        
        if self.hash[root.val] > self.max_count:
            self.max_count = self.hash[root.val]
            self.res = [root.val]
        if self.hash[root.val] == self.max_count and root.val not in self.res:
            self.res.append(root.val)

        self.dfs(root.right)

