#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (39.09%)
# Total Accepted:    431.8K
# Total Submissions: 1.1M
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# strs[i] 仅由小写英文字母组成
# 
# 
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        # method 1
        str_len = list(map(len, strs))
        if all(str_len) == 0 or str_len == []:
            return ''
        shortest_len = min(str_len)
        shortest_strs = list(filter(lambda x: len(x) == shortest_len, strs))

        for shortest_str in shortest_strs:
            for i in reversed(range(shortest_len+1)):
                target_str = shortest_str[0: i]
                if all([target_str == s[0: i] for s in strs]):
                    return target_str
        """

        """
        # method 2
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
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        min_len = 201
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)

        for i in reversed(range(min_len+1)):
            if len(set([s[0: i] for s in strs])) == 1:
                return strs[0][0: i]
        return ''





