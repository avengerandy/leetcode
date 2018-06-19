class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<int> degreeList;
        vector<int> nodeVal;
        vector<vector<int>> ansVector;
        
        for (int i = 0; i < n; i++) {
            degreeList.push_back(i);
        }
        
        for (int degree : degreeList) {
            this->unbalancedTreeTraversal(ansVector, nodeVal, degreeList, degree);
        }
        return this->convertToAns(ansVector, n);
    }
    
    void unbalancedTreeTraversal(vector<vector<int>> &ansVector, vector<int> nodeVal, vector<int> degreeList, int degreeNumber) {
        nodeVal.push_back(degreeNumber);
        degreeList.erase(std::remove(degreeList.begin(), degreeList.end(), degreeNumber), degreeList.end());
        if (degreeList.empty() && this->isSave(nodeVal)) {
            ansVector.push_back(nodeVal);
            return;
        }
        for (int degree : degreeList) {
            if (degree != degreeNumber + 1 && degree != degreeNumber - 1) {
                unbalancedTreeTraversal(ansVector, nodeVal, degreeList, degree);
            }
        }
        return;
    }
    
    vector<vector<string>> convertToAns(vector<vector<int>> ansVector, int total) {
        vector<vector<string>> ansStringVector;
        for (auto& intVec : ansVector) {
            vector<string> subVector(total, string(total, '.'));
            for (int i = 0; i < total; i++){
                subVector[i][intVec[i]] = 'Q';
            }
            ansStringVector.push_back(subVector);
        }
        return ansStringVector;
    }
    
    bool isSave(vector<int> queenVector) {
        for (int i = 0; i < queenVector.size(); i++) {
            for (int j = i + 1; j < queenVector.size(); j++) {
                if(abs(queenVector[j] - queenVector[i]) == abs(j - i)) return false;
            }
        }
        return true;
    }
};