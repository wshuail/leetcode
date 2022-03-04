#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#
# https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (73.99%)
# Total Accepted:    118.6K
# Total Submissions: 160.4K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
# 
# 
# 
# 示例：
# 
# 输入："Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
# 
# 
# 
# 
# 提示：
# 
# 
# 在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
# 
# 
#
class Solution:
    def reverseWords(self, s: str) -> str:
        # return ' '.join([word[::-1] for word in s.split(' ')])
        left = -1
        res = ''
        for i in range(len(s)):
            if left < 0 and s[i] != ' ':
                left = i
            if left >= 0 and s[i] == ' ' and i != len(s)-1:
                res += s[left: i][::-1]
                res += ' '
                left = -1
            if left >= 0 and i == len(s)-1:
                res += s[left: i+1][::-1]
        return res
