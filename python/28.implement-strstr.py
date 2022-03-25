#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (39.59%)
# Total Accepted:    281.8K
# Total Submissions: 711.3K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
# 
# 示例 1:
# 
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 
# 
# 说明:
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
# 
#
class Solution:
    def _build_next(self, needle):
        _next = [0]*len(needle)
        _next[0] = -1
        i, j = 0, -1
        while i < len(needle)-1:
            if j == -1 or needle[i]==needle[j]:
                i += 1
                j += 1
                _next[i] = j
            else:
                j = _next[j]
        return _next
    
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack[0: len(needle)] == needle:
            return 0

        _next = self._build_next(needle)

        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = _next[j]

            if j == len(needle):
                return i-j
        
        return -1


    """
    def build_next(self, needle):
        j = 0
        _next = [0]*len(needle)
        for i in range(2, len(needle)):
            while (j>0 and needle[i] != needle[j+1]):
                j = _next[j]
            if needle[i] == needle[j+1]:
                j += 1
            _next[i] = j
        return _next

    def strStr(self, haystack: str, needle: str) -> int:
        if haystack[0: len(needle)] == needle:
            return 0
        
        haystack_len = len(haystack)
        needle_len = len(needle)
        haystack = " " + haystack
        needle = " " + needle
        _next = self.build_next(needle)
        j = 0
        for i in range(1, haystack_len+1):
            while (j>0 and haystack[i] != needle[j+1]):
                j = _next[j]
            if haystack[i] == needle[j+1]:
                j += 1
            if j == needle_len:
                return i-needle_len
        return -1
    """
    
    """
    def strStr(self, haystack: str, needle: str) -> int:
        # method 1
        for i in range(haystack_len-needle_len+1):
            if haystack[i: i+needle_len] == needle:
                return i
        return -1
    """







"""
sol = Solution()
# haystack = "aabba"
# needle = "bba"
haystack = "ababaabbbbababbaabaaabaabbaaaabbabaabbbbbbabbaabbabbbabbbbbaaabaababbbaabbbabbbaabbbbaaabbababbabbbabaaabbaabbabababbbaaaaaaababbabaababaabbbbaaabbbabb"
haystack = haystack[92-6: ]
needle = "abbabbbabaa"
print ('haystack: {}, needle: {}'.format(haystack, needle))
idx = sol.strStr(haystack, needle)
print (idx)
"""



