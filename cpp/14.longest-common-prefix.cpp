/*
 * @lc app=leetcode.cn id=14 lang=cpp
 *
 * [14] 最长公共前缀
 *
 * https://leetcode-cn.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (41.05%)
 * Total Accepted:    727.7K
 * Total Submissions: 1.7M
 * Testcase Example:  '["flower","flow","flight"]'
 *
 * 编写一个函数来查找字符串数组中的最长公共前缀。
 * 
 * 如果不存在公共前缀，返回空字符串 ""。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：strs = ["flower","flow","flight"]
 * 输出："fl"
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：strs = ["dog","racecar","car"]
 * 输出：""
 * 解释：输入不存在公共前缀。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= strs.length <= 200
 * 0 <= strs[i].length <= 200
 * strs[i] 仅由小写英文字母组成
 * 
 * 
 */
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string common_prefix;
        
        if (strs.size() == 0){
            return common_prefix;
        }
        
        if (strs.size() == 1){
            return strs[0];
        }
        
        int min_len = 201;
        for (int i=0; i<strs.size(); ++i){
            if (strs[i].size() < min_len){
                min_len = strs[i].size();
            }
        }

        for (int i=0; i<min_len; ++i){
            set<char> s;
            for (int j=0; j<strs.size(); ++j){
                s.insert(strs[j][i]);
            }
            if (s.size() == 1){
                common_prefix += strs[0][i];
            } else {
                return common_prefix;
            }
        }
        
        return common_prefix;

    }
};
