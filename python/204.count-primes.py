#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (35.67%)
# Total Accepted:    125.9K
# Total Submissions: 329.9K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
# 
# 
# 示例 2：
# 
# 输入：n = 0
# 输出：0
# 
# 
# 示例 3：
# 
# 输入：n = 1
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 5 * 10^6
# 
# 
#
class Solution:
    def countPrimes(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        digits = [1]*n
        digits[0] = digits[1] = 0

        for i in range(2, int(n**0.5)+1):
            if digits[i] == 1:
                for j in range(i+i, n, i):
                    digits[j] = 0

        return sum(digits)






