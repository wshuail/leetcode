#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#
# https://leetcode-cn.com/problems/base-7/description/
#
# algorithms
# Easy (49.95%)
# Total Accepted:    23.4K
# Total Submissions: 46.8K
# Testcase Example:  '100'
#
# 给定一个整数，将其转化为7进制，并以字符串形式输出。
# 
# 示例 1:
# 
# 
# 输入: 100
# 输出: "202"
# 
# 
# 示例 2:
# 
# 
# 输入: -7
# 输出: "-10"
# 
# 
# 注意: 输入范围是 [-1e7, 1e7] 。
# 
#
class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = 1 if num >= 0 else -1
        res = ""
        num = abs(num)
        while num >= 7:
            remain = num%7
            res += str(remain)
            num //= 7
        res += str(num)

        return "-" + res[::-1] if sign < 0 else res[::-1]

"""
num = -7
sol = Solution()
res = sol.convertToBase7(num)
print (res)
"""
