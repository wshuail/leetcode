#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 20. Valid Parentheses
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
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










