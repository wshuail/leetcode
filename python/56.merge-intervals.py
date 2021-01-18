#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (43.44%)
# Total Accepted:    181.1K
# Total Submissions: 411.6K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
# 
# 
# 
# 示例 1:
# 
# 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2:
# 
# 输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
# 注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。
# 
# 
# 
# 提示：
# 
# 
# intervals[i][0] <= intervals[i][1]
# 
# 
#

class Solution:
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    def merge(self, intervals):
        intervals.sort(key=lambda interval: interval[0])
        for interval in intervals:
            if interval[0] > interval[1]:
                intervals.remove(interval)
        res = []
        for i in range(len(intervals)):
            if len(res) == 0:
                res.append(intervals[i])
            else:
                if res[-1][0] <= intervals[i][0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], intervals[i][1])
                else:
                    res.append(intervals[i])
        return res

if __name__ == '__main__':
    sol = Solution()
    # intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [[1,4],[4,5]]
    # print (sol.merge(intervals))

