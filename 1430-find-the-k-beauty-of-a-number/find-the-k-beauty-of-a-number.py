class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        left=0
        right=k
        count=0
        nums=str(num)
        while right <= len(nums):
            if int(nums[left:right])!=0 and num%int(nums[left:right])==0:
                count+=1
            right+=1
            left+=1
        return count


        