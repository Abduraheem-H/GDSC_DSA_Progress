class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.binSearch(nums,target,True)
        right=self.binSearch(nums,target,False)
        return [left,right]
    def binSearch(self,nums,target,status):
       
        left = 0
        right = len(nums) - 1
        idx=-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                idx=mid
                if status:
                    right=mid-1
                else:
                    left=mid+1

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return idx



#print(Solution.searchRange(Solution, [5, 7, 7, 8, 8, 10], 7))
