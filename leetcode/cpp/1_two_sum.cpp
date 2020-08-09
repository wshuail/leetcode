#include <iostream>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std; 


class Solution{
    public:
    vector<int> two_sum(vector<int> & nums, int target){
    unordered_map<int, int> m;
    for (int i=0; nums.size(); ++i){
        if (m.count(target-nums[i])){
                return {i, m[target-nums[i]]};
                }
        m[nums[i]] = i;
        }
    return {};
    }
};


int main(){
    Solution *Two_Sum = new Solution();
    vector<int> nums={2, 7, 11, 15};
    int target = 9;
	vector<int> result = Two_Sum->two_sum(nums, target);
    for (int i=0; i<result.size(); ++i){
        cout << i << "th value is " << result[i] << endl;
    }
    // delete Two_Sum;
}
