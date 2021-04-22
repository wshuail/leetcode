#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (39.95%)
# Total Accepted:    388.4K
# Total Submissions: 972.1K
# Testcase Example:  '[1,3]\n[2]'
#
# <p>给定两个大小分别为 <code>m</code> 和 <code>n</code> 的正序（从小到大）数组 <code>nums1</code> 和
# <code>nums2</code>。请你找出并返回这两个正序数组的 <strong>中位数</strong> 。</p>
# 
# <p> </p>
# 
# <p><strong>示例 1：</strong></p>
# 
# <pre>
# <strong>输入：</strong>nums1 = [1,3], nums2 = [2]
# <strong>输出：</strong>2.00000
# <strong>解释：</strong>合并数组 = [1,2,3] ，中位数 2
# </pre>
# 
# <p><strong>示例 2：</strong></p>
# 
# <pre>
# <strong>输入：</strong>nums1 = [1,2], nums2 = [3,4]
# <strong>输出：</strong>2.50000
# <strong>解释：</strong>合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
# </pre>
# 
# <p><strong>示例 3：</strong></p>
# 
# <pre>
# <strong>输入：</strong>nums1 = [0,0], nums2 = [0,0]
# <strong>输出：</strong>0.00000
# </pre>
# 
# <p><strong>示例 4：</strong></p>
# 
# <pre>
# <strong>输入：</strong>nums1 = [], nums2 = [1]
# <strong>输出：</strong>1.00000
# </pre>
# 
# <p><strong>示例 5：</strong></p>
# 
# <pre>
# <strong>输入：</strong>nums1 = [2], nums2 = []
# <strong>输出：</strong>2.00000
# </pre>
# 
# <p> </p>
# 
# <p><strong>提示：</strong></p>
# 
# <ul>
# <li><code>nums1.length == m</code></li>
# <li><code>nums2.length == n</code></li>
# <li><code>0 <= m <= 1000</code></li>
# <li><code>0 <= n <= 1000</code></li>
# <li><code>1 <= m + n <= 2000</code></li>
# <li><code>-10<sup>6</sup> <= nums1[i], nums2[i] <= 10<sup>6</sup></code></li>
# </ul>
# 
# <p> </p>
# 
# <p><strong>进阶：</strong>你能设计一个时间复杂度为 <code>O(log (m+n))</code> 的算法解决此问题吗？</p>
# 
#
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        print (nums)
        if len(nums)%2==0:
            res = (nums[len(nums)//2-1] + nums[len(nums)//2])/2
        if len(nums)%2==1:
            res = nums[len(nums)//2]
        return res

"""
nums1 = [1, 2]
nums2 = [3, 4]
sol = Solution()
print (sol.findMedianSortedArrays(nums1, nums2))
"""
