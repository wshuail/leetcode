#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 9. Palindrome Number

# Determine whether an integer is a palindrome. Do this without extra space.


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            return str(x) == str(x)[::-1]
        return False


