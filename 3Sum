class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = {}
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            complements = {}
            
            for j in range(i + 1, len(nums)):
                complement = target - nums[j]
                
                if complement in complements:
                    triplet = [nums[i], nums[complements[complement]], nums[j]]
                    triplet.sort()  # Sort to ensure consistent ordering
                    triplet_key = tuple(triplet)
                    if triplet_key not in triplets:
                        triplets[triplet_key] = triplet
                
                complements[nums[j]] = j
        
        return list(triplets.values())
