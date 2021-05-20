#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (77.42%)
# Total Accepted:    246.6K
# Total Submissions: 318.3K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0:
            return []
        path, res = [], []
        used = [False for _ in range(size)]
        self.dfs(nums=nums, depth=0, size=size, path=path, res=res, used=used)
        return res

    def dfs(self, nums, depth, size, path, res, used):
        if len(path) == size:
            res.append(path[:])
        
        for index in range(size):
            if not used[index]:
                used[index] = True
                path.append(nums[index])
                self.dfs(nums=nums, depth=depth+1, size=size, path=path, res=res, used=used)
                used[index] = False
                path.pop()

