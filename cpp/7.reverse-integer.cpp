/*
 * @lc app=leetcode.cn id=7 lang=cpp
 *
 * [7] 整数反转
 *
 * https://leetcode-cn.com/problems/reverse-integer/description/
 *
 * algorithms
 * Easy (35.22%)
 * Total Accepted:    974.4K
 * Total Submissions: 2.8M
 * Testcase Example:  '123'
 *
 * 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
 * 
 * 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
 * 假设环境不允许存储 64 位整数（有符号或无符号）。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：x = 123
 * 输出：321
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：x = -123
 * 输出：-321
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：x = 120
 * 输出：21
 * 
 * 
 * 示例 4：
 * 
 * 
 * 输入：x = 0
 * 输出：0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * -2^31 
 * 
 * 
 */
#include <iostream>
using namespace std;


class Solution {
public:
    int reverse(int x) {
        // std::cout << "INT_MAX: " << INT_MAX << "INT_MIN: " << INT_MIN << '\n' << std::endl;

        int res = 0;
        while (x){
            int remain = x%10;
            // std::cout << "res: " << res << '\n' << std::endl;
            if (res > INT_MAX/10 || res < INT_MIN/10) return 0;
            res = res*10 + remain;
            x /= 10;
        }

        if ((res >= INT_MIN) && (res <= INT_MAX)){
            return res;
        } else {
            return 0;
        }

    }
};

/*
int main(){
    int x = -2147483412;
    Solution sol;
    int res = sol.reverse(x);
    std::cout << res << '\n' << std::endl;
}
*/



