#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (63.11%)
# Total Accepted:    168.1K
# Total Submissions: 266K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
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
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0:
            return []
        nums.sort()
        used = [False for _ in range(size)]
        path, res = [], []
        self.dfs(nums=nums, depth=0, size=size, path=path, res=res, used=used)
        return res

    def dfs(self, nums, depth, size, path, res, used):
        if depth==size:
            res.append(path[:])
            return

        for index in range(size):
            if not used[index]:
                if index>0 and nums[index]==nums[index-1] and not used[index-1]:
                    continue

                used[index] = True
                path.append(nums[index])
                self.dfs(nums=nums, depth=depth+1, size=size, path=path, res=res, used=used)
                used[index] = False
                path.pop()



