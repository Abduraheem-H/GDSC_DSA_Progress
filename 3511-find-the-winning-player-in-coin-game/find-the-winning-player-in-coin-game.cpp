class Solution {
public:
    string losingPlayer(int x, int y) {
        
        int maxTurns = min(x, y / 4);
        
        if (maxTurns % 2 == 1) {
            return "Alice";
        } else {
            return "Bob";
        }
    }
};
