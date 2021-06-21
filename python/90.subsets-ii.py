#
# @lc app=leetcode.cn id=90 lang=python
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (63.39%)
# Total Accepted:    116.1K
# Total Submissions: 183.2K
# Testcase Example:  '[1,2,2]'
#
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0]
# 输出：[[],[0]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10 
# 
# 
# 
# 
#
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        path, res = [], []
        begin = 0
        self.dfs(nums, begin, path, res)
        return res

    def dfs(self, nums, begin, path, res):
        # print ('before: {}'.format(path))
        res.append(path[:])
        # print ('res: {}'.format(res))
        for i in range(begin, len(nums)):
            if i > begin and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            # print ('after: {}'.format(path))
            self.dfs(nums, i+1, path, res)
            path.pop()

"""
sol = Solution()
res = sol.subsetsWithDup([1, 2, 2])
print (res)
"""



