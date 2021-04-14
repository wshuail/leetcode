#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
# https://leetcode-cn.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (55.32%)
# Total Accepted:    75.1K
# Total Submissions: 135.6K
# Testcase Example:  '"abccccdd"'
#
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
# 
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
# 
# 注意:
# 假设字符串的长度不会超过 1010。
# 
# 示例 1: 
# 
# 
# 输入:
# "abccccdd"
# 
# 输出:
# 7
# 
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
# 
# 
#
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for l in s:
            if l in d:
                d[l] += 1
            else:
                d[l] = 1
        odd = False
        res = 0
        for v in d.values():
            if v % 2 == 1 and odd is True:
                res += v-1
            if v % 2 == 1 and odd is False:
                odd = True
                res += v
            if v % 2 == 0:
                res += v
        return res


"""
s = "abccccdd"
sol = Solution()
print (sol.longestPalindrome(s))
"""
                





