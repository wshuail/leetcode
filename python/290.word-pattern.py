#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#
# https://leetcode-cn.com/problems/word-pattern/description/
#
# algorithms
# Easy (45.83%)
# Total Accepted:    70.1K
# Total Submissions: 153.1K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
# 
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
# 
# 示例1:
# 
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
# 
# 示例 2:
# 
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
# 
# 示例 3:
# 
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
# 
# 示例 4:
# 
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
# 
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
# 
#
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        # return len(set(zip(pattern, s))) == len(set(pattern)) == len(set(s)) and len(pattern) == len(s)
        if len(pattern) != len(s):
            return False
        d1, d2 = {}, {}
        for i, p in enumerate(pattern):
            if p in d1 and d1[p] != s[i]:
                return False
            if s[i] in d2 and d2[s[i]] != p:
                return False
            d1[p] = s[i]
            d2[s[i]] = p
        return True

"""
pattern = "abba"
s = "dog cat cat dog"
sol = Solution()
print (sol.wordPattern(pattern, s))
"""



