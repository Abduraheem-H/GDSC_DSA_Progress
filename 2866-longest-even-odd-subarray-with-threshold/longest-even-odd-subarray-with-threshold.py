class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        length = 0
        left = 0
        while left < len(nums):
            if nums[left] % 2 == 0 and nums[left] <= threshold:
                right = left + 1
                while right < len(nums) and nums[right] <= threshold:
                    if nums[right - 1] % 2 != nums[right] % 2:
                        length = max(length, right - left + 1)
                        right += 1
                    else:
                        break
                length = max(length, right - left)  
                left = right
            else:
                left += 1
        return length
