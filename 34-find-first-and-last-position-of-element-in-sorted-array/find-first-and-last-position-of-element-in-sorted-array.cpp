class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left = binSearch(nums, target, true);
        int right = binSearch(nums, target, false);
        return {left, right};
    }

private:
    int binSearch(vector<int>& nums, int target, bool findFirst) {
        int left = 0;
        int right = nums.size() - 1;
        int idx = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                idx = mid;
                if (findFirst) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return idx;
    }
};
