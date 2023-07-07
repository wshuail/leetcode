#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (47.35%)
# Total Accepted:    267.8K
# Total Submissions: 555.3K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr]
# ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 
# 
# 示例 2：
# 
# 
# 输入：target = 4, nums = [1,4,4]
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# 
# 
# 
# 
# 进阶：
# 
# 
# 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
# 
# 
#

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_len = 10**5+1
        sum_ = 0
        for right in range(len(nums)):
            sum_ += nums[right]
            while sum_ >= target:
                sum_ -= nums[left]
                if right-left+1 < min_len:
                    min_len = right - left + 1
                left += 1
        return min_len if min_len < 10**5+1 else 0


if __name__ == '__main__':
    sol = Solution()
    # target = 7
    # nums = [2,3,1,2,4,3]
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    print(sol.minSubArrayLen(target, nums))








