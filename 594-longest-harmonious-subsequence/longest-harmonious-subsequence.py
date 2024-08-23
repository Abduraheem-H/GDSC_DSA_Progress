class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hash_table = Counter(nums)
        print(hash_table)

        count = 0
        for num in set(nums):
            if num + 1 in hash_table:
                sum = hash_table[num] + hash_table[num + 1]
                count = max(count, sum)
        return count
# print(Solution.findLHS(Solution, [4, 5, 4, 4]))
