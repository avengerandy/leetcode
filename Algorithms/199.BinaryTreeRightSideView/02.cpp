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
    
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        if (root == nullptr) return ans;
        int maxLevel = 0;
        this->treeLevelOrder(root, 1, maxLevel, ans);
        return ans;
    }
    
    void treeLevelOrder(TreeNode* root, int level, int &maxLevel, vector<int> &ans) {
        if (level > maxLevel) {
            maxLevel++;
            ans.push_back(root->val);
        }
        if (root->right != nullptr) this->treeLevelOrder(root->right, level+1, maxLevel, ans);
        if (root->left != nullptr) this->treeLevelOrder(root->left, level+1, maxLevel, ans);
        return;
    }
};