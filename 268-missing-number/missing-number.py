class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        counter=Counter(nums)
        max_length=len(nums)+1

        for i in range(max_length):
            if i not in counter:
                return i
        