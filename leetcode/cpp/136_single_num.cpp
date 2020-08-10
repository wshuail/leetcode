#include <iostream>
#include <vector>
using std::vector;

class Solution {
    public:
        int singleNumber(vector<int>& nums) {
            typedef vector<int>::size_type vec_sz;
            int ans = nums[0];
            for (vec_sz i=1; i<nums.size(); ++i){
                ans = nums[i]^ans;
            }
            return ans;
        }
};


int main(){
    using std::cout;
    using std::endl;
    
    vector<int> nums = {1, 2, 3, 2, 1, 3, 4, 5, 4};
    // Solution* sol = new Solution();
    // int ans = sol->singleNumber(nums);
    Solution sol;
    int ans = sol.singleNumber(nums);
    cout << "the unique number is: " << ans << endl;
}
