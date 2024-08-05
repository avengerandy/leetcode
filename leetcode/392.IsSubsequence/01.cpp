class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s == "") return true;
        auto sitr = s.begin();
        for (auto titr = t.begin(); titr < t.end(); titr++) {
            if (*titr == *sitr) {
                sitr++;
                if (sitr == s.end()) return true; 
            }
        }
        return false;
    }
};
