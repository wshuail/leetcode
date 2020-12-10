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
        if len(s) == 1:
            return s
        anchor = 0
        result, tmp = '', ''
        while anchor < len(s):
            left = anchor - 1
            right = anchor + 1
            while right < len(s) and s[anchor] == s[right]:
                tmp = s[anchor: right+1]
                right += 1
                # print ('tmp1: {}'.format(tmp))
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # print (left, right)
                tmp = s[left: right+1]
                left -= 1
                right += 1
                # print ('tmp2: {}'.format(tmp))
            anchor += 1
            if len(tmp) > len(result):
                result = tmp
        if len(result) == 0:
            result = s[0]
        return result

sol = Solution()
x = sol.longestPalindrome('ab')
# print (x)
