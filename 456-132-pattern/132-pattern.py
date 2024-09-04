class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        mini=float("inf")

        for num in nums:
            while stack and num>=stack[-1][0]:
                stack.pop()
            if stack and stack[-1][1]<num:
                return True
            stack.append([num,mini])
            mini=min(mini,num)
        return False



        