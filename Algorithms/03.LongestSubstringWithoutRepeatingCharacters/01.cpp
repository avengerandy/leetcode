class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLength = 0;
        int tmpLength = 0;
        auto start = s.begin() - 1;
        map<int, string::iterator> tmp;
        for(auto itr = s.begin(); itr < s.end(); itr++) {
            auto tmpFind = tmp.find(*itr);
            if(tmpFind != tmp.end() && tmpFind->second > start) {
                start = tmpFind->second;
                tmpLength = itr - start;
            } else {
                tmpLength++;
            }
            tmp[*itr] = itr;
            maxLength = max(tmpLength, maxLength);
        }
        return maxLength;
    }
};
