#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (63.56%)
# Total Accepted:    341.4K
# Total Submissions: 535.8K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 
# 示例:
# 
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 
# 说明:
# 
# 
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
# 
# 
#
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        # method 1
        idx = -1
        for i in range(len(nums)):
            if idx < 0 and nums[i] == 0:
                idx = i
            if idx >= 0 and nums[i] != 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        """

        """
        # method 2
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        for i in range(idx, len(nums)):
            nums[i] = 0
        """

        """
        # method 3
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            elif zero_count > 0:
                nums[i-zero_count] = nums[i]
                nums[i] = 0
        """

        # method 4
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1


"""
nums = [0,1,0,3,12]
sol = Solution()
sol.moveZeroes(nums)
"""
        

