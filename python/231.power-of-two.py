#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (48.97%)
# Total Accepted:    105K
# Total Submissions: 213.4K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
# 
# 示例 1:
# 
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
# 
# 示例 2:
# 
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
# 
# 示例 3:
# 
# 输入: 218
# 输出: false
# 
#
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        while n >= 2:
            if n%2 == 1:
                return False
            if n <= 2 and n%2 == 0:
                return True
            n = n//2
        """
        # return bool(!(n & (n-1)))
        return bin(n)[2] == '1' and '1' not in bin(n)[3:]
