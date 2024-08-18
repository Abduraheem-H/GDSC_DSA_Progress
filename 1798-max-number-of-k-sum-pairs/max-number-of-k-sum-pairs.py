class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        hash_map = {}
        count = 0

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        for num in nums:
            value = k - num

            
            if hash_map[num] > 0 and hash_map.get(value, 0) > 0:
                
                if num == value and hash_map[num] < 2:
                    continue

                count += 1
                hash_map[num] -= 1
                hash_map[value] -= 1

        return count
