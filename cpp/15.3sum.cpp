/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 *
 * https://leetcode-cn.com/problems/3sum/description/
 *
 * algorithms
 * Medium (33.72%)
 * Total Accepted:    795.3K
 * Total Submissions: 2.3M
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0
 * 且不重复的三元组。
 * 
 * 注意：答案中不可以包含重复的三元组。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [-1,0,1,2,-1,-4]
 * 输出：[[-1,-1,2],[-1,0,1]]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = []
 * 输出：[]
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：nums = [0]
 * 输出：[]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 
 * -10^5 
 * 
 * 
 */
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> results;
        sort(nums.begin(), nums.end());
        for (int i=0; i<nums.size()-2; ++i){
            if (i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            vector<int> result;
            int left = i+1;
            int right = nums.size()-1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0){
                    result = {nums[i], nums[left], nums[right]};
                    results.push_back(result);
                    left += 1;
                    right -= 1;
                    while (left < right && nums[left] == nums[left-1]){
                        left += 1;
                    }
                    while (left < right && nums[right] == nums[right+1]){
                        right -= 1;
                    }
                } else if (sum>0){
                    right -= 1;
                } else {
                    left += 1;
                }
            }
        }
        return results;

    }
};
