#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std; 


class Solution{
    public:
    vector<vector<int>> three_sum(vector<int> &nums){
        vector<vector<int>> results;
        sort(nums.begin(), nums.end());
        for (int i=0; i<nums.size()-2; ++i){
            cout << i << endl;
            while (i > 0 && nums[i] == nums[i-1]){
                i += 1;
            }
            vector<int> result;
            int left = i+1;
            int right = nums.size()-1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                cout << i << " " << " " << nums[i] << " " << nums[left] << " " << nums[right] << endl;
                if (sum == 0){
                    result = {nums[i], nums[left], nums[right]};
                    results.push_back(result);
                    left += 1;
                    right -= 1;
                    while (nums[left] == nums[left-1]){
                        left += 1;
                    }
                    while (nums[right] == nums[right+1]){
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


int main(){
    Solution sol;
    //vector<int> nums={-1,0,1,2,-1,-4};
    vector<int> nums={-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0};
	vector <vector<int>> results = sol.three_sum(nums);
    for (int i=0; i<results.size(); ++i){
        vector<int> result = results[i];
        for (int j=0; j<result.size(); ++j){
            cout << j << "th value is " << result[j] << endl;
        }
    }
}
