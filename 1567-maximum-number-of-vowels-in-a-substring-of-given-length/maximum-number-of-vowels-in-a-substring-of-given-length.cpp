class Solution {
public:
    int maxVowels(string s, int k) {
        auto isVowel = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                   c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
        };
        
        int maxVowelCount = 0;
        int currentVowelCount = 0;
        
        for (int i = 0; i < k; i++) {
            if (isVowel(s[i])) {
                currentVowelCount++;
            }
        }
        maxVowelCount = currentVowelCount;
        
        for (int i = k; i < s.size(); i++) {
            if (isVowel(s[i - k])) {
                currentVowelCount--;
            }
            if (isVowel(s[i])) {
                currentVowelCount++;
            }
            maxVowelCount = max(maxVowelCount, currentVowelCount);
        }
        
        return maxVowelCount;
    }
};
