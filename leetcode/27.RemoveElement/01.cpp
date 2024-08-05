class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        for (auto itr = nums.begin(); itr != nums.end();) {
            if (*itr == val) {
                nums.erase(itr);
            } else {
                itr++;
            }
        }
        return nums.size();
    }
};