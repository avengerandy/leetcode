class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) return 1;
        vector<int> ans = {1, 2};
        for (int i = 2; i < n; i++) {
            ans[1] = ans[1] + ans[0];
            ans[0] = ans[1] - ans[0];
        }
        return ans[1];
    }
};