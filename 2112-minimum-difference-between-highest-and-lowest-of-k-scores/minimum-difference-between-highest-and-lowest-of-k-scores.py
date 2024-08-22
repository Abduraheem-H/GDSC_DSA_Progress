class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        right=left+k-1
        minimum_sum=float("inf")
        while right<len(nums):
            current_sum=nums[right]-nums[left]
            minimum_sum=min(current_sum,minimum_sum)
            right+=1
            left+=1
        return minimum_sum



        