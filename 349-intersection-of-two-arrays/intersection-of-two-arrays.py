class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter=Counter(nums1)
        ans=set()
        for num in nums2:
            if num in counter:
                ans.add(num)
        return list(ans)

        