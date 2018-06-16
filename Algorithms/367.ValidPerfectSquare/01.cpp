class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num == 1) return true; 
        if(num <= 0) return false; 
        for(int i = 2; i <= num/2; i++) {
            if(i*i == num) return true;
            if(i*i > num) return false;
        }
        return false;
    }
};