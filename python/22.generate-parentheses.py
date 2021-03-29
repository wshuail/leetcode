#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (76.70%)
# Total Accepted:    218.4K
# Total Submissions: 284.7K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：["()"]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#
class Solution:
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n: int) -> List[str]:
        def generate(s='', left=0, right=0):
            if len(s) == 2*n:
                self.res.append(s)
                return
            if left < n:
                generate(s+'(', left+1, right)
            if right < left:
                generate(s+')', left, right+1)
        
        generate()
        
        return self.res
