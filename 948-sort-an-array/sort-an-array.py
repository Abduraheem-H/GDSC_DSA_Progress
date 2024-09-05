class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(left_ptr, right_ptr):
            if left_ptr >= right_ptr:
                return
            
            mid = (left_ptr + right_ptr) // 2
            mergeSort(left_ptr, mid)
            mergeSort(mid + 1, right_ptr)
            helper(left_ptr, mid, right_ptr)
        
        def helper(left_ptr, mid, right_ptr):
            left = left_ptr
            right = mid + 1
            temp = []
            
            while left <= mid and right <= right_ptr:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            
            while left <= mid:
                temp.append(nums[left])
                left += 1
            
            while right <= right_ptr:
                temp.append(nums[right])
                right += 1
            
            for i in range(len(temp)):
                nums[left_ptr + i] = temp[i]
        
        mergeSort(0, len(nums) - 1)
        return nums
