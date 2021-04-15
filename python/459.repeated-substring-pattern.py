#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#
# https://leetcode-cn.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (51.03%)
# Total Accepted:    66.8K
# Total Submissions: 130.7K
# Testcase Example:  '"abab"'
#
# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
# 
# 示例 1:
# 
# 
# 输入: "abab"
# 
# 输出: True
# 
# 解释: 可由子字符串 "ab" 重复两次构成。
# 
# 
# 示例 2:
# 
# 
# 输入: "aba"
# 
# 输出: False
# 
# 
# 示例 3:
# 
# 
# 输入: "abcabcabcabc"
# 
# 输出: True
# 
# 解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
# 
# 
#
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        for i in range(1, len(s)//2+1):
            if (len(s)-i)%i == 0:
                substr = s[0: i]
                substrs = [s[j: j+i] for j in range(i, len(s), i)]
                if list(set(substrs)) == [substr]:
                    return True
        return False
        """
        return s in (s+s)[1: -1]

"""
s = "abcabcabcabc"
sol = Solution()
print (sol.repeatedSubstringPattern(s))
"""
