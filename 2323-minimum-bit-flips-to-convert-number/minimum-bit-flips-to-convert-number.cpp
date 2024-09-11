class Solution {
public:
    int minBitFlips(int start, int goal) {
        int xorResult = start ^ goal;
        int flips = 0;
        while (xorResult > 0) {
            flips += xorResult & 1;
            xorResult >>= 1;
        }
        return flips;
    }
};
