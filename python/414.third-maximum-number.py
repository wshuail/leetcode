#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
# https://leetcode-cn.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (35.60%)
# Total Accepted:    49K
# Total Submissions: 136.6K
# Testcase Example:  '[3,2,1]'
#
# 给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[3, 2, 1]
# 输出：1
# 解释：第三大的数是 1 。
# 
# 示例 2：
# 
# 
# 输入：[1, 2]
# 输出：2
# 解释：第三大的数不存在, 所以返回最大的数 2 。
# 
# 
# 示例 3：
# 
# 
# 输入：[2, 2, 3, 1]
# 输出：1
# 解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
# 此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。
# 
# 
# 
# 提示：
# 
# 
# 1 
# -2^31 
# 
# 
# 
# 
# 进阶：你能设计一个时间复杂度 O(n) 的解决方案吗？
# 
#
from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        nums = list(set(nums))
        nums.sort(reverse=True)
        return nums[2] if len(nums)>=3 else nums[0]
        """
        min_int = -2**31-1
        first, second, third = min_int, min_int, min_int
        for num in nums:
            if num > first:
                first, second, third = num, first, second
            if first > num > second:
                first, second, third = first, num, second
            if second > num > third:
                first, second, third = first, second, num
        return third if third > min_int else first

"""
nums = [3, 2, 1]
sol = Solution()
sol.thirdMax(nums)
"""
