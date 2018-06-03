class Solution {
public:
    int missingNumber(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int i = 0;
        for(auto itr = nums.begin(); itr < nums.end(); itr++, i++) {
            if(*itr != i) {
                return i;
            }
        }
        return i;
    }
};