#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.81%)
# Total Accepted:    168.5K
# Total Submissions: 367.8K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 
# 
# 示例：
# 
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
# 
# 
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        marker = nums[0] + nums[1] + nums[2]
        diff = abs(target-marker)
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            anchor = nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                three_sum = anchor + nums[left] + nums[right]
                abs_diff = abs(three_sum - target)
                if abs_diff < diff:
                    marker = three_sum
                    diff = abs_diff
                if three_sum < target:
                    left += 1
                else:
                    right -= 1
        return marker
