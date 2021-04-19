#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#
# https://leetcode-cn.com/problems/keyboard-row/description/
#
# algorithms
# Easy (69.82%)
# Total Accepted:    25.6K
# Total Submissions: 36.4K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。
# 
# 美式键盘 中：
# 
# 
# 第一行由字符 "qwertyuiop" 组成。
# 第二行由字符 "asdfghjkl" 组成。
# 第三行由字符 "zxcvbnm" 组成。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：words = ["Hello","Alaska","Dad","Peace"]
# 输出：["Alaska","Dad"]
# 
# 
# 示例 2：
# 
# 
# 输入：words = ["omk"]
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：words = ["adsdf","sfd"]
# 输出：["adsdf","sfd"]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# words[i] 由英文字母（小写和大写字母）组成
# 
# 
#
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        d = {}
        for letter in "qwertyuiop":
            d[letter] = 1
        for letter in "asdfghjkl":
            d[letter] = 2
        for letter in "zxcvbnm":
            d[letter] = 3
        res = []
        for word in words:
            if len(list(set([d[letter.lower()] for letter in word]))) == 1:
                res.append(word)
        return res
