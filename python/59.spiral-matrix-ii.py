#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (79.96%)
# Total Accepted:    103.2K
# Total Submissions: 129.3K
# Testcase Example:  '3'
#
# 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：[[1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, u = 0, 0
        w, h = n-1, n-1
        matrix = [[0]*n for _ in range(n)]
        nums = [i+1 for i in range(n**2)]
        index = 0

        while True:
            for i in range(l, w+1):
                matrix[u][i] = nums[index]
                index += 1
            u += 1
            if u > h:
                break

            for i in range(u, h+1):
                matrix[i][w] = nums[index]
                index += 1
            w -= 1
            if l > w:
                break

            for i in range(w, l-1, -1):
                matrix[h][i] = nums[index]
                index += 1
            h -= 1
            if u > h:
                break

            for i in range(h, u-1, -1):
                matrix[i][l] = nums[index]
                index += 1
            l += 1
            if l > w:
                break

        return matrix

"""
n = 3
sol = Solution()
res = sol.generateMatrix(n)
print (res)
assert res == [[1,2,3],[8,9,4],[7,6,5]]
"""







