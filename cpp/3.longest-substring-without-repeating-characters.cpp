//  Name: Luke Wang
//  Email: oopswangsl@gmail.com
//  Date: 2023-03-16



//  Given a string s, find the length of the longest substring without repeating characters.
//   
//  Example 1:
//  
//  Input: s = "abcabcbb"
//  Output: 3
//  Explanation: The answer is "abc", with the length of 3.
//  
//  Example 2:
//  
//  Input: s = "bbbbb"
//  Output: 1
//  Explanation: The answer is "b", with the length of 1.
//  
//  Example 3:
//  
//  Input: s = "pwwkew"
//  Output: 3
//  Explanation: The answer is "wke", with the length of 3.
//  Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
//  
//   
//  Constraints:
//  
//  0 <= s.length <= 5 * 104
//  s consists of English letters, digits, symbols and spaces.
//  

#include <iostream>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0, right = 1;
        int max_len = 0, cur_len = 0;
        unordered_set<char> sub_s;

        for (right=0; right<s.length(); right++){
            cur_len++;
            if (sub_s.count(s[right])){
                while (sub_s.count(s[right])){
                    sub_s.erase(s[left]);
                    left++;
                    cur_len--;
                }    
            }
            sub_s.insert(s[right]);
            max_len = max(cur_len, max_len);
        }

        return max_len;
        
    }
};





