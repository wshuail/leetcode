#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (62.59%)
# Total Accepted:    83.9K
# Total Submissions: 134K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 3
# 输出: [1,3,3,1]
# 
# 
# 进阶：
# 
# 你可以优化你的算法到 O(k) 空间复杂度吗？
# 
#
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        res = []
        for i in range(rowIndex+1):
            row = [None for _ in range(i+1)]
            row[0], row[-1] = 1, 1
            for j in range(1, i):
                row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)

        return res[rowIndex]
        """
        rowIndex += 1
        res = [1]*rowIndex
        if rowIndex <= 2:
            return res
        for i in range(rowIndex):
            for j in reversed(range(1, i)):
                res[j] = res[j] + res[j-1]
        return res


# sol = Solution()
# print (sol.getRow(5))
