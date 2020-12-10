#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (32.37%)
# Total Accepted:    423.4K
# Total Submissions: 1.3M
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s
        start = 0
        max_len = 1
        for i in range(1, len(s)):
            odd = s[i-max_len-1: i+1]
            even = s[i-max_len: i+1]
            if i-max_len-1>=0 and odd==odd[::-1]:
                start = i-max_len-1
                max_len += 2
            if i-max_len >= 0 and even == even[::-1]:
                start = i-max_len
                max_len += 1
        return s[start: start+max_len]

# sol = Solution()
# x = sol.longestPalindrome('abad')
# print (x)
