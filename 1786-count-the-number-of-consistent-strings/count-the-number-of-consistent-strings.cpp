class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int count = 0;
        unordered_set<char> allowedChars(allowed.begin(), allowed.end());

        for (const string& word : words) {
            bool consistent = true;
            for (char c : word) {
                if (!allowedChars.count(c)) {
                    consistent = false;
                    break;
                }
            }
            if (consistent) {
                count++;
            }
        }

        return count;
    }
};