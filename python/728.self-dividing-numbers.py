#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#
# https://leetcode-cn.com/problems/self-dividing-numbers/description/
#
# algorithms
# Easy (76.04%)
# Total Accepted:    38.5K
# Total Submissions: 51.4K
# Testcase Example:  '1\n22'
#
# 自除数 是指可以被它包含的每一位数整除的数。
# 
# 
# 例如，128 是一个 自除数 ，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
# 
# 
# 自除数 不允许包含 0 。
# 
# 给定两个整数 left 和 right ，返回一个列表，列表的元素是范围 [left, right] 内所有的 自除数 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：left = 1, right = 22
# 输出：[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# 
# 
# 示例 2:
# 
# 
# 输入：left = 47, right = 85
# 输出：[48,55,66,77]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= left <= right <= 10^4
# 
# 
#
class Solution:
    def is_self_dividing(self, num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for s in str_num:
            if num%int(s) != 0:
                return False
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [num for num in range(left, right+1) if self.is_self_dividing(num)]















