class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        auto itr = digits.end() - 1;
        while (*itr == 9) {
            *itr = 0;
            if (itr == digits.begin()){
                digits.insert(digits.begin(), 1);
                return digits;
            }
            itr--;
        }
        *itr += 1;
        return digits;
    }
};