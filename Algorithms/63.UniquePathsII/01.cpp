class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int n = obstacleGrid.size();
        int m = obstacleGrid[0].size();
        vector<int> dp;
        int flag = 1;
        for (int i = 0; i < m; i++) {
            if (obstacleGrid[0][i] == 1) {
                flag = 0;
            }
            dp.push_back(flag);
        }
        for (int j = 1; j < n; j++) {
            if (obstacleGrid[j][0] == 1) {
                dp[0] = 0;
            }
            for (int i = 1; i < m; i++) {
                if (obstacleGrid[j][i] == 1) {
                    dp[i] = 0;
                    continue;
                }
                dp[i] = dp[i] + dp[i - 1];
            }
        }
        return *(dp.end() - 1);
    }
};