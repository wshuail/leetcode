#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std; 


class Solution{
    public:
    vector<int> two_sum(vector<int> & nums, int target){
        vector<int> result;
        unordered_map<int, int> m;
        for (int i=0; i< nums.size(); ++i){
            if (m.count(target-nums[i])){
                result.push_back(i);
                result.push_back(m[target-nums[i]]);
                return result;
            }
        m[nums[i]] = i;
        }
    return result;
    }
};


int main(){
    Solution sol;
    vector<int> nums={2, 7, 11, 15};
    int target = 9;
	vector<int> result = sol.two_sum(nums, target);
    for (int i=0; i<result.size(); ++i){
        cout << i << "th value is " << result[i] << endl;
    }
}
