class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if num % 2 == 0:
                if num in hash_map:
                    hash_map[num] += 1
                else:
                    hash_map[num] = 1
        print(hash_map)
        max = 0
        k = 0
        for key in hash_map.keys():
            if hash_map[key] == max:
                if key < k:
                    k = key

            elif hash_map[key] > max:
                max = hash_map[key]
                k = key
        if len(hash_map) == 0:
            return -1
        else:
            return k


# solution = Solution()
# print(solution.mostFrequentEven([0, 1, 2, 2, 4, 4, 1]))
