class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums.size() == 0 || target <= *nums.begin()) {
            return 0;
        }
        int index = 1;
        for(auto itr = nums.begin() + 1; itr < nums.end(); itr++, index++) {
            if (target <= *itr) {
                return index;
            }
        }
        return index;
    }
};