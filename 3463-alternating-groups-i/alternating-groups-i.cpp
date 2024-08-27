class Solution {
public:
    int numberOfAlternatingGroups(std::vector<int>& colors) {
        int n = colors.size();
        int count = 0;

        for (int i = 0; i < n; ++i) {
            
            int left = colors[i];
            int middle = colors[(i + 1) % n];
            int right = colors[(i + 2) % n];

            if (left != middle && middle != right) {
                count++;
            }
        }

        return count;
    }
};
