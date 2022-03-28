#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#
# https://leetcode-cn.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (60.97%)
# Total Accepted:    37.1K
# Total Submissions: 59.1K
# Testcase Example:  '5'
#
# 给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 5
# 输出：true
# 解释：5 的二进制表示是：101
# 
# 
# 示例 2：
# 
# 
# 输入：n = 7
# 输出：false
# 解释：7 的二进制表示是：111.
# 
# 示例 3：
# 
# 
# 输入：n = 11
# 输出：false
# 解释：11 的二进制表示是：1011.
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 2^31 - 1
# 
# 
#
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)[2: ]
        if len(s) == 1:
            return True
        marker = s[0]
        i = 1
        while i < len(s):
            if s[i] == marker:
                return False
            else:
                marker = s[i]
                i += 1
        return True

