class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        new_nums = set(nums)
        num=list(new_nums)
       
        if len(new_nums) < 3:
            return max(num)
        num.sort(reverse=True)
        return num[2]


# solution = Solution()
# print(solution.thirdMax([2, 2, 3, 1]))
