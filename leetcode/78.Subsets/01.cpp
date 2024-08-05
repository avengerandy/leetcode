class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> powerset;
        vector<int> emptySet;
        vector<int>::const_iterator itr;
        powerset.push_back(emptySet);
        for (itr = nums.cbegin(); itr < nums.cend(); itr++) {
            int count = powerset.size();
            for (int i = 0; i < count; i++) {
                vector<int> newSet;
                newSet.reserve(powerset[i].size() + 1); // preallocate memory
                newSet.insert(newSet.end(), powerset[i].cbegin(), powerset[i].cend());
                newSet.push_back(*itr);
                powerset.push_back(newSet);
            }
        }
        return powerset;
    }
};
