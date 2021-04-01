#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#
# https://leetcode-cn.com/problems/find-the-difference/description/
#
# algorithms
# Easy (69.51%)
# Total Accepted:    85.2K
# Total Submissions: 122.7K
# Testcase Example:  '"abcd"\n"abcde"'
#
# 给定两个字符串 s 和 t，它们只包含小写字母。
# 
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
# 
# 请找出在 t 中被添加的字母。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "abcd", t = "abcde"
# 输出："e"
# 解释：'e' 是那个被添加的字母。
# 
# 
# 示例 2：
# 
# 输入：s = "", t = "y"
# 输出："y"
# 
# 
# 示例 3：
# 
# 输入：s = "a", t = "aa"
# 输出："a"
# 
# 
# 示例 4：
# 
# 输入：s = "ae", t = "aea"
# 输出："a"
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length <= 1000
# t.length == s.length + 1
# s 和 t 只包含小写字母
# 
# 
#
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        d1, d2 = {}, {}
        for x in s:
            if x in d1:
                d1[x] += 1
            else:
                d1[x] = 1
        for x in t:
            if x in d2:
                d2[x] += 1
            else:
                d2[x] = 1
        for k, v in d2.items():
            if k not in d1 or v > d1[k]:
                return k
        """
        s = s + t
        x = 0
        for i in s:
            x ^= ord(i)
        return chr(x)

