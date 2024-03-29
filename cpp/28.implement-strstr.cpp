/*
 * @lc app=leetcode.cn id=28 lang=cpp
 *
 * [28] 实现 strStr()
 *
 * https://leetcode-cn.com/problems/implement-strstr/description/
 *
 * algorithms
 * Easy (40.54%)
 * Total Accepted:    563.3K
 * Total Submissions: 1.4M
 * Testcase Example:  '"hello"\n"ll"'
 *
 * 实现 strStr() 函数。
 * 
 * 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0
 * 开始）。如果不存在，则返回  -1 。
 * 
 * 
 * 
 * 说明：
 * 
 * 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
 * 
 * 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf()
 * 定义相符。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：haystack = "hello", needle = "ll"
 * 输出：2
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：haystack = "aaaaa", needle = "bba"
 * 输出：-1
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：haystack = "", needle = ""
 * 输出：0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 
 * haystack 和 needle 仅由小写英文字符组成
 * 
 * 
 */
#include <string>
#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    int strStr(string haystack, string needle) {
        int m = haystack.length(), n = needle.length();
        if (haystack.substr(0, n) == needle){
            return 0;
        }

        /*
        // method 1
        for (int i=0; i < m-n+1; ++i){
            // std::cout << "i: " << i << " substr: " << haystack.substr(i, n) << "\n";
            if (haystack.substr(i, n) == needle){
                return i;
            }
        }
        return -1;
        */

        // KMP
        haystack.insert(haystack.begin(), ' ');
        needle.insert(needle.begin(), ' ');
        vector<int> next(n+1);
        int j = 0;
        
        for (int i=2; i<=n; ++i){
            while (j>0 && needle[i] != needle[j+1]){
                j = next[j];
            }
            if (needle[i] == needle[j+1]){
                j++;
            }
            next[i] = j;
        }
        /*
        std::cout << "next size: " << next.size() << "\n";
        
        for (int i=0; i<next.size(); ++i){
            std::cout << "idx: " << next[i] << "\n";
        }
        */

        for (int i=1, j=0; i<=m; ++i){
            while (j>0 && haystack[i] != needle[j+1]){
                j = next[j];
            }
            if (haystack[i] == needle[j+1]){
                j++;
            }
            if (j==n){
                return i-n;
            }
        }

        return -1;

    }
};

/*
int main(){
    Solution sol;
    // string haystack = "aaabbab", needle="ab";
    string haystack = "aabbababbabbbabaaabbaabbabababbbaaaaaaababbabaababaabbbbaaabbbabb", needle="abbabbbabaa";
    std::cout << "res: " << needle.size() << "\n";
    int res = sol.strStr(haystack, needle);
    std::cout << "res: " << res << "\n";
}
*/
