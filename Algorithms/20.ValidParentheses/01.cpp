class Solution {
public:
    bool isValid(string s) {
        string::iterator itr;
        stack<char> parenthesesStack;
        map<char, char> parenthesesMap;
        parenthesesMap[')'] = '(';
        parenthesesMap[']'] = '[';
        parenthesesMap['}'] = '{';
        for (itr = s.begin(); itr < s.end(); itr++) {
            if (parenthesesMap.find(*itr) == parenthesesMap.end()) {
                parenthesesStack.push(*itr);
            } else if (!parenthesesStack.empty()) {
                return false;
            } else if (parenthesesMap[*itr] == parenthesesStack.top()) {
                parenthesesStack.pop();
            } else {
                return false;
            }
        }
        return parenthesesStack.empty();
    }
};