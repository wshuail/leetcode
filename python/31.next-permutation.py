#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (36.17%)
# Total Accepted:    124.3K
# Total Submissions: 342.8K
# Testcase Example:  '[1,2,3]'
#
# 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 
# 必须 原地 修改，只允许使用额外常数空间。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[1,3,2]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,2,1]
# 输出：[1,2,3]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1,1,5]
# 输出：[1,5,1]
# 
# 
# 示例 4：
# 
# 
# 输入：nums = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return nums
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = len(nums)-1
            while j>i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1: ] = nums[i+1: ][::-1]
        return nums

"""
# nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
nums = [3, 2, 1]
sol = Solution()
res = sol.nextPermutation(nums)
print (res)
"""


