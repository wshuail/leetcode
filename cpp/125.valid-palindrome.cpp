/*
 * @lc app=leetcode.cn id=125 lang=cpp
 *
 * [125] 验证回文串
 *
 * https://leetcode-cn.com/problems/valid-palindrome/description/
 *
 * algorithms
 * Easy (47.27%)
 * Total Accepted:    337K
 * Total Submissions: 716.9K
 * Testcase Example:  '"A man, a plan, a canal: Panama"'
 *
 * 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
 * 
 * 说明：本题中，我们将空字符串定义为有效的回文串。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入: "A man, a plan, a canal: Panama"
 * 输出: true
 * 解释："amanaplanacanalpanama" 是回文串
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: "race a car"
 * 输出: false
 * 解释："raceacar" 不是回文串
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * 字符串 s 由 ASCII 字符组成
 * 
 * 
 */
class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> str;
        for (int i=0; i<s.size(); i++){
            if (isalnum(s[i])){
                str.push_back(tolower(s[i]));
            }
        }

        int left=0, right=str.size()-1;
        while (left < right){
            if (str[left] != str[right]){
                return false;
            }
            left++;
            right--;
        }

        return true;

    }
};
