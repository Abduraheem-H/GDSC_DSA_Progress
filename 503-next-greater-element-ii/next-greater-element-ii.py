class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        stack = []
        ptr = 0

        while ptr < len(nums) * 2:
            index = ptr % len(nums)
            while stack and nums[stack[-1]] < nums[index]:
                i = stack.pop()
                ans[i] = nums[index]

            stack.append(index)
            ptr += 1
        
        return ans
