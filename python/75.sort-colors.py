#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
# https://leetcode-cn.com/problems/sort-colors/description/
#
# algorithms
# Medium (58.21%)
# Total Accepted:    200.3K
# Total Submissions: 344K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [0]
# 输出：[0]
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
# n == nums.length
# 1 
# nums[i] 为 0、1 或 2
# 
# 
# 
# 
# 进阶：
# 
# 
# 你可以不使用代码库中的排序函数来解决这道题吗？
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
# 
# 
#
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        idx = 0
        for num in [0, 1, 2]:
            count = d.get(num, 0)
            nums[idx: idx+count] = [num for _ in range(count)]
            idx += count
