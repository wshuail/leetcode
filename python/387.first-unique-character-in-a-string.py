#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (51.19%)
# Total Accepted:    173.1K
# Total Submissions: 334.5K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 
# 
# 
# 示例：
# 
# s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
# 
# 
# 
# 
# 提示：你可以假定该字符串只包含小写字母。
# 
#
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for l in s:
            if l in d:
                d[l] += 1
            else:
                d[l] = 1
        for i, l in enumerate(s):
            if d[l] == 1:
                return i
        return -1
