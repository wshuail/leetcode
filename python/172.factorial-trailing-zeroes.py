#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#
# https://leetcode-cn.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (41.30%)
# Total Accepted:    68.8K
# Total Submissions: 162.4K
# Testcase Example:  '3'
#
# 给定一个整数 n，返回 n! 结果尾数中零的数量。
# 
# 示例 1:
# 
# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
# 
# 示例 2:
# 
# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
# 
# 说明: 你算法的时间复杂度应为 O(log n) 。
# 
#
class Solution:
    def trailingZeroes(self, n: int) -> int:
        r = 0
        while n >= 5:
            n = n//5
            r += n
        return r
        """
        res = str(self.factorial(n))[::-1]
        if res[0]=='0':
            for i in range(1, len(res)):
                if res[i] != '0':
                    return i
        else:
            return 0

    def factorial(self, n):
        if n==0 or n==1:
            return 1
        else:
            return n*self.factorial(n-1)
        """

"""
n = 10
sol = Solution()
print (sol.trailingZeroes(10))
"""
