#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (76.87%)
# Total Accepted:    174.2K
# Total Submissions: 226.6K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 
# 示例:
# 
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        path, res = [], []
        begin = 1
        self.dfs(n, k, begin, path, res)
        return res

    def dfs(self, n, k, begin, path, res):
        if len(path) == k:
            res.append(path[:])
            return

        for i in range(begin, n-(k-len(path))+2):
        # for i in range(begin, n+1):
            path.append(i)
            self.dfs(n, k, i+1, path, res)
            path.pop()


"""
sol = Solution()
res = sol.combine(4, 2)
print (res)
"""




