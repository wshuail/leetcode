#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 67. Add Binary
# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_int, b_int = int(a, 2), int(b, 2)
        return bin(a_int+b_int)[2:]



