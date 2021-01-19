#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (69.78%)
# Total Accepted:    146K
# Total Submissions: 209.1K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
#
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            rows = [None for _ in range(i+1)]
            rows[0], rows[-1] = 1, 1
            for j in range(1, i):
                rows[j] = res[i-1][j-1] + res[i-1][j]
            res.append(rows)

        return res


