class Solution {
public:
    vector<int> missingRolls(vector<int>& a, int b, int n) {
        int m = a.size();
        int c = (m + n) * b;
        int d = accumulate(a.begin(), a.end(), 0);
        int e = c - d;
        
        if (e < n || e > 6 * n) {
            return {};
        }
        
        vector<int> res(n, 1);
        e -= n;
        
        for (int i = 0; i < n && e > 0; ++i) {
            int f = min(5, e);
            res[i] += f;
            e -= f;
        }
        
        return res;
    }
};
