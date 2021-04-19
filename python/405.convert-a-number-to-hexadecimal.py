#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#
# https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal/description/
#
# algorithms
# Easy (51.74%)
# Total Accepted:    21.5K
# Total Submissions: 41.4K
# Testcase Example:  '26'
#
# 给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。
# 
# 注意:
# 
# 
# 十六进制中所有字母(a-f)都必须是小写。
# 十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
# 给定的数确保在32位有符号整数范围内。
# 不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
# 
# 
# 示例 1：
# 
# 
# 输入:
# 26
# 
# 输出:
# "1a"
# 
# 
# 示例 2：
# 
# 
# 输入:
# -1
# 
# 输出:
# "ffffffff"
# 
# 
#
class Solution:
    def toHex(self, num: int) -> str:
        num = num&0xFFFFFFFF
        d = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        res = ''
        while num >= 16:
            remain = num%16
            res += str(remain) if remain < 10 else d[remain]
            num = num//16
        res += str(num) if num < 10 else d[num]
        return res[::-1]