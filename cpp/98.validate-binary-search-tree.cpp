/*
 * @lc app=leetcode.cn id=98 lang=cpp
 *
 * [98] 验证二叉搜索树
 *
 * https://leetcode-cn.com/problems/validate-binary-search-tree/description/
 *
 * algorithms
 * Medium (34.46%)
 * Total Accepted:    292.9K
 * Total Submissions: 849.7K
 * Testcase Example:  '[2,1,3]'
 *
 * 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
 * 
 * 假设一个二叉搜索树具有如下特征：
 * 
 * 
 * 节点的左子树只包含小于当前节点的数。
 * 节点的右子树只包含大于当前节点的数。
 * 所有左子树和右子树自身必须也是二叉搜索树。
 * 
 * 
 * 示例 1:
 * 
 * 输入:
 * ⁠   2
 * ⁠  / \
 * ⁠ 1   3
 * 输出: true
 * 
 * 
 * 示例 2:
 * 
 * 输入:
 * ⁠   5
 * ⁠  / \
 * ⁠ 1   4
 * / \
 * 3   6
 * 输出: false
 * 解释: 输入为: [5,1,4,null,null,3,6]。
 * 根节点的值为 5 ，但是其右子节点值为 4 。
 * 
 * 
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private: 
    TreeNode* pre;

public:
    bool isValidBST(TreeNode* root) {
        /*
         * method 1
        if (root==NULL) return true;
        if (!isValidBST(root->left)) return false;
        if ((pre != NULL) && (pre->val >= root->val)) return false;
        pre = root;
        if (!isValidBST(root->right)) return false;
        return true;
        */

        // method 2
        if (root == NULL) return true;
        
        stack<TreeNode*> q;
        
        while (!q.empty() || root != NULL){
            while (root != NULL){
                q.push(root);
                root = root->left;
            }
            root = q.top();
            q.pop();
            if ((pre != NULL) && (pre->val >= root->val)) return false;
            pre = root;
            root = root->right;
        }
        return true;

    }
};
