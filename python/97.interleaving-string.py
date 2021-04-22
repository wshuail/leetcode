#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#
# https://leetcode-cn.com/problems/interleaving-string/description/
#
# algorithms
# Medium (45.85%)
# Total Accepted:    45.1K
# Total Submissions: 98.3K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# 给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。
# 
# 两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
# 
# 
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| 
# 交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
# 
# 
# 提示：a + b 意味着字符串 a 和 b 连接。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：s1 = "", s2 = "", s3 = ""
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# s1、s2、和 s3 都由小写英文字母组成
# 
# 
#
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        """
        if s1 == '':
            return s2==s3
        if s2 == '':
            return s1==s3
        if s3[0] == s1[0] and s3[0] != s2[0]:
            return self.isInterleave(s1[1:], s2, s3[1:])
        elif s3[0] != s1[0] and s3[0] == s2[0]:
            return self.isInterleave(s1, s2[1:], s3[1:])
        elif s3[0] == s1[0] and s3[0] == s2[0]:
            return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
        else:
            return False
        """
        dp = [[True for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 and j==0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = (dp[i][j-1] and s3[i+j-1]==s2[j-1])
                elif j == 0:
                    dp[i][j] = (dp[i-1][j] and s3[j+i-1]==s1[i-1])
                else:
                    dp[i][j] = ((dp[i-1][j] and s3[i+j-1]==s1[i-1]) or (dp[i][j-1] and s3[i+j-1]==s2[j-1]))
        return dp[-1][-1]

"""
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
# s1, s2, s3 = 'ab', 'ac', 'aabc'
print (s1, s2, s3)
sol = Solution()
print (sol.isInterleave(s1, s2, s3))
"""



