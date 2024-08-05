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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if (root == nullptr) return ans;
        queue<TreeNode*> levelQueue;
        levelQueue.push(root);
        this->treeLevelOrder(levelQueue, ans);
        return ans;
    }
    
    void treeLevelOrder(queue<TreeNode*> levelQueue, vector<vector<int>> &levelOrder) {
        if(levelQueue.empty()) return;
        vector<int> level;
        queue<TreeNode*> NextLevelQueue;
        while(!levelQueue.empty()) {
            TreeNode* node = levelQueue.front();
            levelQueue.pop();
            level.push_back(node->val);
            if (node->left != nullptr) NextLevelQueue.push(node->left);
            if (node->right != nullptr) NextLevelQueue.push(node->right);
        }
        levelOrder.push_back(level);
        this->treeLevelOrder(NextLevelQueue, levelOrder);
        return;
    }
};
