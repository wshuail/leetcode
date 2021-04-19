#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#
# https://leetcode-cn.com/problems/relative-ranks/description/
#
# algorithms
# Easy (55.57%)
# Total Accepted:    16.1K
# Total Submissions: 28.7K
# Testcase Example:  '[5,4,3,2,1]'
#
# 给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold
# Medal", "Silver Medal", "Bronze Medal"）。
# 
# (注：分数越高的选手，排名越靠前。)
# 
# 示例 1:
# 
# 
# 输入: [5, 4, 3, 2, 1]
# 输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# 解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and
# "Bronze Medal").
# 余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
# 
# 提示:
# 
# 
# N 是一个正整数并且不会超过 10000。
# 所有运动员的成绩都不相同。
# 
# 
#
from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = {}
        for idx, s in enumerate(sorted(score, reverse=True)):
            idx += 1
            if idx == 1:
                d[s] = "Gold Medal"
            elif idx == 2:
                d[s] = "Silver Medal"
            elif idx == 3:
                d[s] = "Bronze Medal"
            else:
                d[s] = str(idx)
        return [d[s] for s in score]

"""
score = [5, 4, 3, 2, 1]
sol = Solution()
res = sol.findRelativeRanks(score)
print (res)
"""

