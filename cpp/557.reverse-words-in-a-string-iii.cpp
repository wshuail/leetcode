/*
 * @lc app=leetcode.cn id=557 lang=cpp
 *
 * [557] 反转字符串中的单词 III
 *
 * https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/description/
 *
 * algorithms
 * Easy (74.52%)
 * Total Accepted:    210.3K
 * Total Submissions: 283.2K
 * Testcase Example:  `"Let's take LeetCode contest"`
 *
 * 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s = "Let's take LeetCode contest"
 * 输出："s'teL ekat edoCteeL tsetnoc"
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入： s = "God Ding"
 * 输出："doG gniD"
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 5 * 10^4
 * s 包含可打印的 ASCII 字符。
 * s 不包含任何开头或结尾空格。
 * s 里 至少 有一个词。
 * s 中的所有单词都用一个空格隔开。
 * 
 * 
 */
#include <iostream>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        if (s.size() < 1) return s;
        int left = -1;
        string res = "";
        string tmp;
        for (int i=0; i<s.size(); i++){
            // std::cout << "left: " << left << " i: " << i << " res[i]: " << res[i] << "\n";
            if (left<0 && s[i]!=' '){
                left = i;
            } 
            if (left>=0 && i<s.size()-1 && s[i]==' '){
                string tmp = s.substr(left, i-left);
                reverse(tmp.begin(), tmp.end());
                res += tmp;
                res += " ";
                left = -1;
            }
            if (left>=0 && i==s.size()-1){
                tmp = s.substr(left, i+1-left);
                reverse(tmp.begin(), tmp.end());
                res += tmp;
            }
        }
        return res;
    }
};

/*
int main(){
    Solution sol;
    // string s = "Let's take LeetCode contest";
    string s = "I love u";
    std::cout << s.size() << s[s.size()-1] << "\n";
    string res = sol.reverseWords(s);
    std::cout << res << "\n";
}
*/
