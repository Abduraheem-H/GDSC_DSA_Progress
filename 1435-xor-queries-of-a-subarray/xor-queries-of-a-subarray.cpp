class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int n = arr.size();
        vector<int> prefixXOR(n);  
        vector<int> result;  
        prefixXOR[0] = arr[0];
        for (int i = 1; i < n; i++) {
            prefixXOR[i] = prefixXOR[i - 1] ^ arr[i];
        }
        
      
        for (const auto& query : queries) {
            int l = query[0];  
            int r = query[1];  
            if (l == 0) {
                result.push_back(prefixXOR[r]);  
            } else {
                result.push_back(prefixXOR[r] ^ prefixXOR[l - 1]);  
            }
        }
        
        return result;
    }
};
