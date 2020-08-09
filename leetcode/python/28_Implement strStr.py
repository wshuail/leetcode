#! /usr/bin/env python
# -*- coding: utf-8 -*-


# 28. Implement strStr()
#
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        elif len(haystack) == 0 and len(needle) != 0:
            return -1
        elif len(needle) == 0:
            return 0
        haystack_len = len(haystack)
        needle_len = len(needle)

        for i in range(haystack_len-needle_len+1):
            if haystack[i: i+needle_len] == needle:
                return i
        return -1

