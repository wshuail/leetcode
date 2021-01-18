#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
# Input: "Hello World"
# Output: 5


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = s.split(' ')
        s_list = [word for word in s_list if word != '']
        if not s_list:
            return 0
        else:
            return len(s_list[-1])
