#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (46.80%)
# Total Accepted:    279.3K
# Total Submissions: 596.9K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 你可以假设数组中无重复元素。
# 
# 示例 1:
# 
# 输入: [1,3,5,6], 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [1,3,5,6], 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 输入: [1,3,5,6], 7
# 输出: 4
# 
# 
# 示例 4:
# 
# 输入: [1,3,5,6], 0
# 输出: 0
# 
# 
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        if nums == []:
            return 0
        for i, val in enumerate(nums):
            if val >= target:
                return i
        return len(nums)
        """
        if nums[-1] < target:
            return len(nums)
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

