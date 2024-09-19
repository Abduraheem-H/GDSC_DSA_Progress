


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        left = n - 1
        right = m - 1
        index = m + n - 1

        while left >= 0 and right >= 0:
            if nums1[right] > nums2[left]:
                nums1[index] = nums1[right]
                right -= 1
            else:
                nums1[index] = nums2[left]
                left -= 1
            index -= 1

        while left >= 0:
            nums1[index] = nums2[left]
            left -= 1
            index -= 1

       

#print(Solution.merge(Solution, [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))




