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
        """
        # method 1
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
            while left >= 0 and right < len(s) and s[left] == s[right]:
                tmp = s[left: right+1]
                left -= 1
                right += 1
            anchor += 1
            if len(tmp) > len(result):
                result = tmp
        if len(result) == 0:
            result = s[0]
        return result
        """

        """
        # method 2
        if len(s) < 2 or s == s[::-1]:
            return s
        start = 0
        max_len = 1
        for i in range(1, len(s)):
            odd = s[i-max_len-1: i+1]  # len(odd) = max_len+2
            even = s[i-max_len: i+1]  # len(even) = max_len+1
            if i-max_len-1 >= 0 and odd == odd[::-1]:
                start = i-max_len-1
                max_len += 2
                continue
            if i-max_len >= 0 and even == even[::-1]:
                start = i-max_len
                max_len += 1
        return s[start: start+max_len]
        """

        # method 3
        if len(s) < 2 or s == s[::-1]:
            return s

        res = ''
        for i in range(len(s)):
            # odd
            tmp = self._helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            
            tmp = self._helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def _helper(self, s, left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        return s[left+1: right]





