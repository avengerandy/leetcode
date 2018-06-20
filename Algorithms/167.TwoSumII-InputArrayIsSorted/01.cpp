class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        auto point1 = numbers.cbegin();
        auto point2 = numbers.cend() - 1;
        while (point2 > point1) {
            if(*point1 + *point2 > target) point2--;
            else if(*point1 + *point2 < target) point1++;
            else return vector<int> {point1 - numbers.cbegin() + 1, point2 - numbers.cbegin() + 1};
        }
    }
};
