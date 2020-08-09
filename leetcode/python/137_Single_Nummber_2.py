#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Given an array of integers, every element appears three times except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        statis = {}
        for num in nums:
            if num in statis.keys():
                if statis[num] == 2:
                    del statis[num]
                else:
                    statis[num] += 1
            else:
                statis[num] = 1
        return list(statis.keys())[0]
