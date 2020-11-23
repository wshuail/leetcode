class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum == 0:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1
        
        return res



if __name__ == '__main__':
    sol = Solution()
    nums_list = [[0, 0, 0, 0], [-1,0,1,2,-1,-4], [-2,0,0,2,2], [-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]]
    for nums in nums_list:
        results = sol.threeSum(nums)
        print (results)
