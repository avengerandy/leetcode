class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> numsMap;
        map<int, int> ::iterator jItr;
        int numSize = nums.size();
        for (int i = 0; i < numSize; i++) {
            numsMap[nums[i]] = i;
        }
        for (int i = 0; i < numSize; i++) {
            jItr = numsMap.find(target - nums[i]);
            if (jItr != numsMap.end()) {
                int j = jItr->second;
                if (i != j) {
                    return vector<int>{i, j};
                }
            }
        }
    }
};