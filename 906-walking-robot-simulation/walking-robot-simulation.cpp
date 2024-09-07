class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        vector<pair<int, int>> dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        set<pair<int, int>> obs_set;
        for (const auto& obs : obstacles) {
            obs_set.insert({obs[0], obs[1]});
        }
        int pos_x = 0, pos_y = 0, direction = 0, max_dist = 0;

        for (int cmd : commands) {
            if (cmd == -2) {
                direction = (direction + 3) % 4;
            } else if (cmd == -1) {
                direction = (direction + 1) % 4;
            } else {
                for (int i = 0; i < cmd; ++i) {
                    int next_x = pos_x + dir[direction].first;
                    int next_y = pos_y + dir[direction].second;
                    if (obs_set.find({next_x, next_y}) == obs_set.end()) {
                        pos_x = next_x;
                        pos_y = next_y;
                        max_dist = max(max_dist, pos_x * pos_x + pos_y * pos_y);
                    } else {
                        break;
                    }
                }
            }
        }

        return max_dist;
    }
};
