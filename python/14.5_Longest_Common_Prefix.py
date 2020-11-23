#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str_len = list(map(len, strs))
        if all(str_len) == 0 or str_len == []:
            return ''
        shortest_len = min(str_len)
        shortest_strs = list(filter(lambda x: len(x) == shortest_len, strs))

        for shortest_str in shortest_strs:
            target_len = shortest_len

            while target_len >= 0:
                len_diff = shortest_len - target_len
                for j in range(len_diff + 1):
                    target_str = shortest_str[j: target_len + j]
                    if all(target_str in single_str for single_str in strs):
                        return target_str

                target_len -= 1








