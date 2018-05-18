class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int numSize = nums.size();
        for (int i = 0; i < numSize; i++) {
            for (int j = i + 1; j < numSize; j++) {
                if (nums[i] + nums[j] == target) {
                    return vector<int> {i, j};
                }
            }
        }
    }
};