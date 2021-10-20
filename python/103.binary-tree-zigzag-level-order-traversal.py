#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (57.14%)
# Total Accepted:    170.9K
# Total Submissions: 299.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回锯齿形层序遍历如下：
# 
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        queue = [root]
        res = []
        while queue:
            level_res = []
            next_level_queue = []
            for node in queue:
                level_res.append(node.val)
                if node.left:
                    next_level_queue.append(node.left)
                if node.right:
                    next_level_queue.append(node.right)
            res.append(level_res)
            queue = next_level_queue
        pointers = [i%2+1 for i in range(len(res))]
        pointers = [i if i==1 else -1 for i in pointers]
        res = [r[::pointer] for r, pointer in zip(res, pointers)]

        return res

