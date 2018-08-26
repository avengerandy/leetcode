class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> powerset;
        set<vector<int>> ansSet;
        vector<int> emptySet;
        vector<int>::const_iterator itr;
        powerset.push_back(emptySet);
        ansSet.insert(emptySet);
        sort(nums.begin(), nums.end()); // make sure duplicates solutions with same order
        for (itr = nums.cbegin(); itr < nums.cend(); itr++) {
            int count = powerset.size();
            for (int i = 0; i < count; i++) {
                vector<int> newSet;
                newSet.reserve(powerset[i].size() + 1); // preallocate memory
                newSet.insert(newSet.end(), powerset[i].cbegin(), powerset[i].cend());
                newSet.push_back(*itr);
                powerset.push_back(newSet);
                ansSet.insert(newSet);
            }
        }
        return vector<vector<int>>{ansSet.begin(),ansSet.end()};
    }
};