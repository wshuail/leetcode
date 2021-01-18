#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (43.30%)
# Total Accepted:    505.3K
# Total Submissions: 1.2M
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#
class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {')': '(', ']': '[', '}': '{'}
        left_paren = ['(', '[', '{']
        tmp_stack = []
        str_len = len(s)
        if str_len > 0 and str_len % 2 == 0:
            for i in range(str_len):
                if s[i] in left_paren:
                    tmp_stack.append(s[i])
                else:
                    if len(tmp_stack) == 0:
                        return False
                    elif valid_dict.get(s[i]) == tmp_stack.pop():
                        continue
                    else:
                        return False

            if len(tmp_stack) == 0:
                return True
            else:
                return False
        else:
            return False


