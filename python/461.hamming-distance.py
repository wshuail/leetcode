#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#
# https://leetcode-cn.com/problems/hamming-distance/description/
#
# algorithms
# Easy (78.54%)
# Total Accepted:    107.5K
# Total Submissions: 135.9K
# Testcase Example:  '1\n4'
#
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
# 
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
# 
# 注意：
# 0 ≤ x, y < 2^31.
# 
# 示例:
# 
# 
# 输入: x = 1, y = 4
# 
# 输出: 2
# 
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
# 
# 上面的箭头指出了对应二进制位不同的位置。
# 
# 
#
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, y = bin(x)[2:], bin(y)[2:]
        x, y = x.zfill(max(len(x), len(y))), y.zfill(max(len(x), len(y)))
        res = 0
        for xl, yl in zip(x, y):
            if xl != yl:
                res += 1
        return res
