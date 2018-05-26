class Solution {
public:
    double myPow(double x, int n) {
        if(n == INT_MIN) {
            return abs(x) == 1.0 ? 1.0 : 0.0;
        }
        if (n < 0) {
            n = -n;
            x = 1/x;
        }
        if (n == 0) return 1.0;
        double temp = myPow(x, n>>1);
        if (n % 2) {
            return temp * temp * x;
        }
        return temp * temp;
    }
};