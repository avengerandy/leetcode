class Solution {
public:
    bool isPalindrome(int x) {
        string rs = to_string(x);
        string s = rs;
        std::reverse(rs.begin(), rs.end());
        return rs == s;
    }
};