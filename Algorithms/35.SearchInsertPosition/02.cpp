class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        int mid = right >> 1;
        while(left <= right) {
            if (nums[mid] > target) {
                right = mid - 1;
            }else if (nums[mid] == target) {
                return mid;
            }else {
                left = mid + 1;
            }
            mid = left + ((right - left) >> 1);
        }
        return left;
    }
};