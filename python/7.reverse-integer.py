#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (34.75%)
# Total Accepted:    559.8K
# Total Submissions: 1.6M
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 
# 
# 注意：
# 
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回
# 0。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：x = 123
# 输出：321
# 
# 
# 示例 2：
# 
# 
# 输入：x = -123
# 输出：-321
# 
# 
# 示例 3：
# 
# 
# 输入：x = 120
# 输出：21
# 
# 
# 示例 4：
# 
# 
# 输入：x = 0
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 
# 
# 
#
class Solution:
    def reverse(self, x: int) -> int:
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




