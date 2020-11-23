#! /usr/bin/env python
# -*- coding: utf-8 -*-


# 202. Happy Number
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer,
# replace the number by the sum of the squares of its digits, and repeat the process until the number
# equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        appeared_num = set()
        while True:
            n_list = list(str(n))
            n_list = list(map(lambda x: x**2, list(map(int, n_list))))
            n = sum(n_list)
            if n == 1:
                return True
            elif n in appeared_num:
                return False
            else:
                appeared_num.add(n)



