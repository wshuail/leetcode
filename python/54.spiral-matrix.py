#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (46.64%)
# Total Accepted:    155.7K
# Total Submissions: 331.3K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -100 
# 
# 
#
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, u = 0, 0
        h, w = len(matrix)-1, len(matrix[0])-1
        res = []

        while True:
            for i in range(l, w+1):
                res.append(matrix[u][i])
            u += 1
            if u > h:
                break
            
            for i in range(u, h+1):
                res.append(matrix[i][w])
            w -= 1
            if w < l:
                break
            
            # for i in range(w, l-1, -1):
            for i in reversed(range(l, w+1)):
                res.append(matrix[h][i])
            h -= 1
            if h < u:
                break
            
            for i in range(h, u-1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > w:
                break

        return res

"""
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[7],[9],[6]]
sol = Solution()
res = sol.spiralOrder(matrix)
print (res)
"""




