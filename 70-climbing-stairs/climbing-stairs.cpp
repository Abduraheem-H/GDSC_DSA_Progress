class Solution {
public:
    int climbStairs(int n) {
        int sum1 = 2;
        int sum2 = 1;
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        int current_sum;
        for (int i = 3; i <= n; i++) {
            current_sum = sum1 + sum2;
            sum2 = sum1;
            sum1 = current_sum;
        }
        return current_sum;
    }
};
