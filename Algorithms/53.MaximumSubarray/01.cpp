class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = numeric_limits<int>::min();
        int nowSum = 0;
        for (auto itr = nums.begin(); itr < nums.end(); itr++) {
            nowSum = max(*itr, nowSum + *itr);
            maxSum = max(maxSum, nowSum);
        }
        return maxSum;
    }
};
