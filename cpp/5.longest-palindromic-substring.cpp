/*
 * @lc app=leetcode.cn id=5 lang=cpp
 *
 * [5] 最长回文子串
 *
 * https://leetcode-cn.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (35.59%)
 * Total Accepted:    887.1K
 * Total Submissions: 2.4M
 * Testcase Example:  '"babad"'
 *
 * 给你一个字符串 s，找到 s 中最长的回文子串。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s = "babad"
 * 输出："bab"
 * 解释："aba" 同样是符合题意的答案。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s = "cbbd"
 * 输出："bb"
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 1000
 * s 仅由数字和英文字母组成
 * 
 * 
 */
#include <string>
#include <iostream>
using namespace std;


class Solution {
private:
    string helper(string s, int left, int right){
        while (left>=0 && right<s.size() && s[left]==s[right]){
            left -= 1;
            right += 1;
        } 
        return s.substr(left+1, right-left-1);
    }

public:
    string longestPalindrome(string s) {
        if (s.size() < 2){
            return s;
        }

        string res;
        for (int i=0; i<s.size(); ++i){
            string odd, even;
            odd = helper(s, i, i);
            if (odd.size() > res.size()){
                res = odd;
            }
            
            even = helper(s, i, i+1);
            if (even.size() > res.size()){
                res = even;
            }
        }
        return res;
    }
};

/*
int main(){
    Solution sol;
    string s = "cbbd";
    string res = sol.longestPalindrome(s);
    std::cout << res << "\n";
}
*/



