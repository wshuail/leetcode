#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#
# https://leetcode-cn.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (43.65%)
# Total Accepted:    59.7K
# Total Submissions: 136.7K
# Testcase Example:  '16'
#
# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
# 
# 进阶：不要 使用任何内置的库函数，如  sqrt 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：num = 16
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：num = 14
# 输出：false
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
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        x = 2
        while x <= num//2:
            if x**2 == num:
                return True
        return False
        """
        t = 1
        while num > 0:
            num -= t
            t += 2
        return num == 0
