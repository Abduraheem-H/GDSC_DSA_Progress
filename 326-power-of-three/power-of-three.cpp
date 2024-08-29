class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n <= 0) {
            return false;
        }
        int result = n / 3;
        if (n == 1) {
            return true;
        } else if (n % 3 == 0) {
            return isPowerOfThree(result);
        } else {
            return false;  
        }
    }
};
