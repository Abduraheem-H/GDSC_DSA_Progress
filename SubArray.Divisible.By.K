class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        hash_sum = {0: 1}  
        for num in nums:
            prefix_sum += num
            remainder= prefix_sum % k

            if remainder in hash_sum:
                count += hash_sum[remainder]
            if remainder in hash_sum:
                hash_sum[remainder] += 1
            else:
                hash_sum[remainder] = 1

        return count

        
