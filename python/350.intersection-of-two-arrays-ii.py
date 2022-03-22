#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (53.72%)
# Total Accepted:    183.4K
# Total Submissions: 339.1K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
# 
# 
# 示例 2:
# 
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]
# 
# 
# 
# 说明：
# 
# 
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
# 我们可以不考虑输出结果的顺序。
# 
# 
# 进阶：
# 
# 
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
# 
# 
#
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        d1, d2, d = dict(), dict(), dict()
        for num in nums1:
            if num in d1:
                d1[num] += 1
            else:
                d1[num] = 1
        for num in nums2:
            if num in d2:
                d2[num] += 1
            else:
                d2[num] = 1

        for k, v in d1.items():
            if k in d2:
                d[k] = min(v, d2[k])
        res = []
        for k, v in d.items():
            res += [k for _ in range(v)]
        return res
        """

        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            else:
                if nums1[i] > nums2[j]:
                    j += 1
                else:
                    i += 1
        return res


"""
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
sol = Solution()
print (sol.intersect(nums1, nums2))

"""

