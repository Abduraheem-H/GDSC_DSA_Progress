class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i in range(len(nums)):
            for j in range(0, len(nums) - i - 1):
                str1 = str(nums[j]) + str(nums[j + 1])
                str2 = str(nums[j + 1]) + str(nums[j])
                if str1 < str2:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return "".join(map(str, nums)) if nums[0] != 0 else "0"



#print(Solution.largestNumber(Solution, [3, 34, 36, 5, 9]))