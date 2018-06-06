class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<int> dp;
        for (int i = 0, score = 0; i < m; i++) {
            score += grid[0][i];
            dp.push_back(score);
        }
        for (int j = 1; j < n; j++) {
            dp[0] += grid[j][0];
            for (int i = 1; i < m; i++) {
                if (dp[i] < dp[i - 1]) {
                    dp[i] = dp[i] + grid[j][i];
                    continue;
                }
                dp[i] = dp[i - 1] + grid[j][i];
            }
        }
        return *(dp.end() - 1);
    }
};