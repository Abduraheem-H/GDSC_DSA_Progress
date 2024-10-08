
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_hash = {"max": None}
        max_count = 0
        for key in counter.keys():
            if max(counter[key],max_count) == counter[key]:
                max_hash["max"] = key
                max_count = counter[key]
        return max_hash["max"]

        