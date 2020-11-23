#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 66. Plus One
#
# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list.
#

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        adder = 1
        for i in reversed(range(len(digits))):
            target = digits[i] + adder
            digits[i] = target % 10
            if target >= 10:
                adder = 1
            else:
                adder = 0
        if adder == 1:
            digits = [1] + digits
        return digits



