#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (68.60%)
# Total Accepted:    228.6K
# Total Submissions: 333.2K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 
# 0 
# 
# 
#
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    continue
                elif i==0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j==0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]



