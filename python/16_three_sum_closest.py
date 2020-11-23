class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        marker = nums[0] + nums[1] + nums[2]
        diff = abs(target-marker)
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            anchor = nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                three_sum = anchor + nums[left] + nums[right]
                abs_diff = abs(three_sum - target)
                if abs_diff < diff:
                    marker = three_sum
                    diff = abs_diff
                if three_sum < target:
                    left += 1
                else:
                    right -= 1
        return marker
