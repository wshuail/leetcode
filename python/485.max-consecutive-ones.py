#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#
# https://leetcode-cn.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (56.95%)
# Total Accepted:    102.4K
# Total Submissions: 171K
# Testcase Example:  '[1,1,0,1,1,1]'
#
# 给定一个二进制数组， 计算其中最大连续 1 的个数。
# 
# 
# 
# 示例：
# 
# 
# 输入：[1,1,0,1,1,1]
# 输出：3
# 解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
# 
# 
# 
# 
# 提示：
# 
# 
# 输入的数组只包含 0 和 1 。
# 输入数组的长度是正整数，且不超过 10,000。
# 
# 
#
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        nums = ''.join([str(num) for num in nums]).split('0')
        num_len = [len(num) for num in nums if num != '']
        if num_len:
            return max(num_len)
        else:
            return 0
        """
        max_len, tmp = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tmp += 1
            else:
                tmp = 0
            max_len = max(max_len, tmp)
        return max_len

"""
nums = [1,1,0,1,1,1]
sol = Solution()
print (sol.findMaxConsecutiveOnes(nums))
"""



