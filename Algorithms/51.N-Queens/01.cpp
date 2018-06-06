class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<int> queenVector;
        vector<vector<int>> ansVector;
        for (int i = 0; i < n; i++) {
            queenVector.push_back(i);
        }
        do {
            bool flag = true;
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    if(abs(queenVector[j] - queenVector[i]) == abs(j - i)){
                        flag = false;
                    }
                    if (!flag) {
                        break;
                    }
                }
                if (!flag) {
                    break;
                }
            }
            if (flag) {
                ansVector.push_back(queenVector);
            }
        } while (next_permutation(queenVector.begin(), queenVector.end()));
        
        vector<vector<string>> ansStringVector;
        for (auto& intVec : ansVector) {
            vector<string> subVector;
            for (int i = 0; i < n; i++) {
                string row = string(n, '.');
                row[intVec[i]] = 'Q';
                subVector.push_back(row);
            }
            ansStringVector.push_back(subVector);
        }
        return ansStringVector;
    }
};