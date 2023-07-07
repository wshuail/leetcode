#  Name: luke
#  Email: oopswangsl@gmail.com
#  Date: 2023-07-07


#  Given a binary array nums, you should delete one element from it.
#  Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
#   
#  Example 1:
#  
#  Input: nums = [1,1,0,1]
#  Output: 3
#  Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
#  
#  Example 2:
#  
#  Input: nums = [0,1,1,1,0,1,1,0,1]
#  Output: 5
#  Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
#  
#  Example 3:
#  
#  Input: nums = [1,1,1]
#  Output: 2
#  Explanation: You must delete one element.
#  
#   
#  Constraints:
#  
#  1 <= nums.length <= 105
#  nums[i] is either 0 or 1.
#  

#  Hints:
#  0: Maintain a sliding window where there is at most one zero on it.


from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        right = 0
        left = 0
        max_len = 0
        zero_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            if zero_count == 1:
                max_len = max(max_len, right - left)
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            right += 1

        if zero_count == 0:
            return len(nums) - 1
        else:
            return max_len



if __name__ == '__main__':
    s = Solution()
    nums = [0,1,1,1,0,1,1,0,1]
    print(s.longestSubarray(nums))
    print ('answer is 5')
    """
    nums = [1,1,0,1]
    print(s.longestSubarray(nums))
    print ('answer is 3')
    nums = [1,1,1]
    print(s.longestSubarray(nums))
    print ('answer is 2')
    """




        
