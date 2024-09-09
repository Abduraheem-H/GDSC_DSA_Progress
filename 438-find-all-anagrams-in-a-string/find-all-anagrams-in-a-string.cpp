class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> result;
        int n = s.size(), m = p.size();
        
        if (n < m) return result;  
        vector<int> pCount(26, 0);
        
        vector<int> sCount(26, 0);
        
        
        for (char c : p) {
            pCount[c - 'a']++;
        }
        
        for (int i = 0; i < n; i++) {
       
            sCount[s[i] - 'a']++;
            
        
            if (i >= m) {
                sCount[s[i - m] - 'a']--;
            }
            

            if (sCount == pCount) {
                result.push_back(i - m + 1);
            }
        }
        
        return result;
    }
};
