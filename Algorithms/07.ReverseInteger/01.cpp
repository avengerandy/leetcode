class Solution {
public:
    int reverse(int x) {
        string sign = x > 0 ? "+" : "-";
        auto s = to_string(x);
        std::reverse(s.begin(), s.end());
        s = sign + s;
        try {
            return stoi(s);
        }catch (const std::out_of_range& error) {
            return 0;
        }
    }
};