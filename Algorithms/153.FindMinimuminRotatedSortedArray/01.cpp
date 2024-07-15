class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        int mid = 0;
        while (left < right) {
            mid = (left + right) / 2;
            if (left == mid) {
                break;
            }
            if (nums[left] <= nums[right]) {
                return nums[left];
            }
            if (nums[left] <= nums[mid]) {
                left = mid;
            } else {
                right = mid;
            }
        }

        int ans = min(nums[left], nums[mid]);
        ans = min(ans, nums[right]);
        return ans;
    }
};
