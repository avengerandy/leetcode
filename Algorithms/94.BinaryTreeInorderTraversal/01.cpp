/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans = {};
        this->inorder(root, &ans);
        return ans;
    }

    void inorder(TreeNode* node, vector<int>* ans) {
        if(node != nullptr) {
            this->inorder(node->left, ans);
            ans->push_back(node->val);
            this->inorder(node->right, ans);
        }
    }
};