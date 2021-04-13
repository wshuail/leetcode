#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (51.22%)
# Total Accepted:    66.7K
# Total Submissions: 129.1K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# 
# 
# 
# 示例 1：
# 
# 输入："hello"
# 输出："holle"
# 
# 
# 示例 2：
# 
# 输入："leetcode"
# 输出："leotcede"
# 
# 
# 
# 提示：
# 
# 
# 元音字母不包含字母 "y" 。
# 
# 
#
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [l for l in s if l in 'aeiouAEIOU'][::-1]
        idx = 0
        s = list(s)
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                s[i] = vowels[idx]
                idx += 1
        s = ''.join(s)
        return s
