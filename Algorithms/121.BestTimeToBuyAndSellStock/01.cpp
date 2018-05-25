class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int begin = numeric_limits<int>::max();
        int sell = 0;
        for(vector<int>::iterator itr = prices.begin(); itr != prices.end(); itr++) {
            begin = min(begin, *itr);
            sell = max(sell, *itr - begin);
        }
        return sell;
    }
};