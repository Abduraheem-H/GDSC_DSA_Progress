class Solution:
    def nextGreaterElement(self,nums1, nums2):
        result = []
        for num in nums1:
            index = nums2.index(num)  
            status = False
            
            for i in range(index + 1, len(nums2)):
                if nums2[i] > num:  
                    result.append(nums2[i])
                    status = True
                    break
            if not status: 
                result.append(-1)
        return result




   