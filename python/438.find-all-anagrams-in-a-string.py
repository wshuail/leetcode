#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (50.18%)
# Total Accepted:    64.9K
# Total Submissions: 129.1K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
# 
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
# 
# 说明：
# 
# 
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
# 
# 
# 示例 1:
# 
# 
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
# 
# 
# 示例 2:
# 
# 
# 输入:
# s: "abab" p: "ab"
# 
# 输出:
# [0, 1, 2]
# 
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
# 
# 
#
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        res = []
        sorted_p = ''.join(sorted(p))
        for i in range(len(s)-len(p)+1):
            if ''.join(sorted(s[i: i+len(p)])) == sorted_p:
                res.append(i)
        return res
        """
        s_counter, p_counter = {}, {}
        s_length, p_length = len(s), len(p)
        res = []

        for letter in p:
            if letter in p_counter:
                p_counter[letter] += 1
            else:
                p_counter[letter] = 1
        
        for letter in s[0: p_length-1]:
            if letter in s_counter:
                s_counter[letter] += 1
            else:
                s_counter[letter] = 1
        # print (p_counter, s_counter)

        for i in range(s_length-p_length+1):
            if s[i+p_length-1] in s_counter:
                s_counter[s[i+p_length-1]] += 1
            else:
                s_counter[s[i+p_length-1]] = 1
            if i-1 >= 0:
                if s_counter[s[i-1]] == 1:
                    del s_counter[s[i-1]]
                else:
                    s_counter[s[i-1]] -= 1
            
            if p_counter == s_counter:
                res.append(i)
        
        return res

"""
s = "cbaebabacd"
p = "abc"
sol = Solution()
print (sol.findAnagrams(s, p))
"""



