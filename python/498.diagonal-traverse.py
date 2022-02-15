#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#
# https://leetcode-cn.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (46.97%)
# Total Accepted:    51.5K
# Total Submissions: 105.8K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,4,7,5,3,6,8,9]
# 
# 
# 示例 2：
# 
# 
# 输入：mat = [[1,2],[3,4]]
# 输出：[1,2,3,4]
# 
# 
# 
# 
# 提示：
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# -10^5 <= mat[i][j] <= 10^5
# 
# 
#
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, col = len(mat), len(mat[0])
        m, n = 0, 0
        res = []
        for i in range(row+col-1):
            if i%2 == 0:
                while m >= 0 and n < col:
                    res.append(mat[m][n])
                    m -= 1
                    n += 1
                if n < col:
                    m += 1
                else:
                    m += 2
                    n -= 1
            else:
                while m < row and n >= 0:
                    res.append(mat[m][n])
                    m += 1
                    n -= 1
                if m < row:
                    n += 1
                else:
                    n += 2
                    m -= 1

        return res
