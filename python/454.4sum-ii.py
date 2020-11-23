#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#
# https://leetcode-cn.com/problems/4sum-ii/description/
#
# algorithms
# Medium (56.73%)
# Total Accepted:    30.6K
# Total Submissions: 53.9K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] +
# D[l] = 0。
# 
# 为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -2^28 到 2^28 - 1
# 之间，最终结果不会超过 2^31 - 1 。
# 
# 例如:
# 
# 
# 输入:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# 
# 输出:
# 2
# 
# 解释:
# 两个元组如下:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
# 
# 
#
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB_dict = {}
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                two_sum = A[i] + B[j]
                if two_sum not in AB_dict:
                    AB_dict[two_sum] = 1
                else:
                    AB_dict[two_sum] += 1
        for i in range(len(C)):
            for j in range(len(D)):
                two_sum = C[i] + D[j]
                counter = AB_dict.get(-two_sum, None)
                if counter is not None:
                    res += counter
        return res       
