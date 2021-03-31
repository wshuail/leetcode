#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# https://leetcode-cn.com/problems/house-robber/description/
#
# algorithms
# Easy (47.34%)
# Total Accepted:    263.2K
# Total Submissions: 545.7K
# Testcase Example:  '[1,2,3,1]'
#
# 
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
# 示例 2：
# 
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400
# 
# 
#
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        marker_1, marker_2, marker = 0, 0, 0
        for i in reversed(range(0, len(nums))):
            res = max(marker_1, nums[i]+marker_2)
            marker_1, marker_2 = res, marker_1
        return res
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        bp = [0 for _ in range(len(nums))]
        bp[0], bp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            bp[i] = max(bp[i-1], nums[i]+bp[i-2])
        return bp[-1]
    
        """
    """
        self.memo = [-1 for _ in range(len(nums))]
        return self.dp(nums, 0)

    def dp(self, nums, index):
        if index >= len(nums):
            return 0
        if self.memo[index] != -1:
            return self.memo[index]
        res = max(self.dp(nums, index+1), nums[index] + self.dp(nums, index+2))
        self.memo[index] = res
        return res
    """

nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
sol = Solution()
print (sol.rob(nums))
