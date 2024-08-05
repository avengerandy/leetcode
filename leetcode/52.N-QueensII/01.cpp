class Solution {
public:
    int totalNQueens(int n) {
        vector<int> degreeList;
        vector<int> nodeVal;
        int totalN = 0;
        for (int i = 0; i < n; i++) {
            degreeList.push_back(i);
        }
        for (int degree : degreeList) {
            this->unbalancedTreeTraversal(totalN, nodeVal, degreeList, degree);
        }
        return totalN; 
    }
    
    void unbalancedTreeTraversal(int &totalN, vector<int> nodeVal, vector<int> degreeList, int degreeNumber) {
        nodeVal.push_back(degreeNumber);
        degreeList.erase(std::remove(degreeList.begin(), degreeList.end(), degreeNumber), degreeList.end());
        if (degreeList.empty()) {
            totalN++;
            return;
        }
        for (int degree : degreeList) {
            if(this->isSaveNow(nodeVal, degree)) {
                unbalancedTreeTraversal(totalN, nodeVal, degreeList, degree);
            }
        }
        return;
    }
    
    bool isSaveNow(vector<int> queenVector, int val) {
        for (int i = 0; i < queenVector.size(); i++) {
            if(abs(val - queenVector[i]) == queenVector.size() - i) return false;
        }
        return true;
    }
};
