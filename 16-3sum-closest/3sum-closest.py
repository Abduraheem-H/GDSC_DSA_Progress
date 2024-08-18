from typing import List


class Solution:
    def threeSumClosest(self,nums: List[int], target: int) -> int:
        nums.sort()
        minimum_value= float('inf')

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(minimum_value- target):
                    minimum_value = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
        return minimum_value


#print(Solution.threeSumClosest([1, -3, 2, 5, -4, 8], 7))
