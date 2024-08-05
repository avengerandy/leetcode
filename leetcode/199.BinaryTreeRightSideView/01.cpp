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
        queue<TreeNode*> levelQueue;
        levelQueue.push(root);
        this->treeLevelOrder(levelQueue, ans);
        return ans;
    }
    
    void treeLevelOrder(queue<TreeNode*> levelQueue, vector<int> &ans) {
        if(levelQueue.empty()) return;
        queue<TreeNode*> NextLevelQueue;
        int levelAns;
        while(!levelQueue.empty()) {
            TreeNode* node = levelQueue.front();
            levelQueue.pop();
            levelAns = node->val;
            if (node->left != nullptr) NextLevelQueue.push(node->left);
            if (node->right != nullptr) NextLevelQueue.push(node->right);
        }
        ans.push_back(levelAns);
        this->treeLevelOrder(NextLevelQueue, ans);
        return;
    }
};