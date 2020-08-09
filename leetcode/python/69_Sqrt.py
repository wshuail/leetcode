#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Implement int sqrt(int x).
# Compute and return the square root of x.


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        g = x
        while g * g - x > 0.00001:
            g = (g + x / g) / 2
        return g
