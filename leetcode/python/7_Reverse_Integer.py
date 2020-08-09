#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 7. Reverse Integer

# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output:  321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -2**31 <= x <= 2**31-1:
            x = str(x)
            if x[0] == '-':
                x = -int(x[:0:-1])
            else:
                x = int(x[::-1])
            if -2 ** 31 <= x <= 2 ** 31 - 1:
                return x
            else:
                return 0
        else:
            return 0



