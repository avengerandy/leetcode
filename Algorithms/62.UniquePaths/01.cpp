class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp;
        for (int i = 0; i < m; i++) {
            dp.push_back(1);
        }
        for (int j = 1; j < n; j++) {
            for (int i = 1; i < m; i++) {
                dp[i] = dp[i] + dp[i - 1];
            }
        }
        return *(dp.end() - 1);
    }
};