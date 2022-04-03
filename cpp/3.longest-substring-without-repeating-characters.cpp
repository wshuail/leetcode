/*
 * @lc app=leetcode.cn id=3 lang=cpp
 *
 * [3] 无重复字符的最长子串
 *
 * https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (38.13%)
 * Total Accepted:    1.6M
 * Total Submissions: 4.2M
 * Testcase Example:  '"abcabcbb"'
 *
 * 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入: s = "abcabcbb"
 * 输出: 3 
 * 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: s = "bbbbb"
 * 输出: 1
 * 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
 * 
 * 
 * 示例 3:
 * 
 * 
 * 输入: s = "pwwkew"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
 * 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 <= s.length <= 5 * 10^4
 * s 由英文字母、数字、符号和空格组成
 * 
 * 
 */
#include <unordered_map>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        /*
        //s[start,end) 前面包含 后面不包含
        unordered_map<char, int> hash;
        int left = 0;
        int right = 0;
        int length = 0;
        int result = 0;
        while (right < int(s.size()))
        {
            char ch = s[right];
            //仅当s[start,end) 中存在s[end]时更新start
            if (hash.find(ch) != hash.end() && hash[ch] >= left)
            {
                left = hash[ch] + 1;
                length = right - left;
            }
            hash[ch] = right;

            right++;
            length++;
            result = max(result, length);
        }
        return result;
        */
        unordered_map<char, int> hash;
        int left = 0;
        int right = 0;
        int length = 0;
        int result = 0;
        while (right < int(s.size())){
            char ch = s[right];
            if (hash.find(ch) != hash.end() && hash[ch] >= left){
                left = hash[ch] + 1;
                length = right - left;
                }
            
            hash[ch] = right;
            
            right++;
            length++;
            result = max(result, length);
        }
        return result;
    }
};

/*
int main(){
    Solution sol;
    string s = "pwwkew";
    int res = sol.lengthOfLongestSubstring(s);
    std::cout << "res: " << res << '\n' << std::endl;
}
*/



