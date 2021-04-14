#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode-cn.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (65.56%)
# Total Accepted:    60.5K
# Total Submissions: 91.6K
# Testcase Example:  '3'
#
# 写一个程序，输出从 1 到 n 数字的字符串表示。
# 
# 1. 如果 n 是3的倍数，输出“Fizz”；
# 
# 2. 如果 n 是5的倍数，输出“Buzz”；
# 
# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
# 
# 示例：
# 
# n = 15,
# 
# 返回:
# [
# ⁠   "1",
# ⁠   "2",
# ⁠   "Fizz",
# ⁠   "4",
# ⁠   "Buzz",
# ⁠   "Fizz",
# ⁠   "7",
# ⁠   "8",
# ⁠   "Fizz",
# ⁠   "Buzz",
# ⁠   "11",
# ⁠   "Fizz",
# ⁠   "13",
# ⁠   "14",
# ⁠   "FizzBuzz"
# ]
# 
# 
#
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(n):
            if (i+1) % 15 == 0:
                res.append("FizzBuzz")
            elif (i+1) % 3 == 0:
                res.append("Fizz")
            elif (i+1) % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i+1))
            
        return res
"""
n=3
sol = Solution()
print (sol.fizzBuzz(n))
"""



