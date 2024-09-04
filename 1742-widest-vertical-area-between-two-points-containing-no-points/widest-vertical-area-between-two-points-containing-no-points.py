class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr=[]
        for pair in points:
            arr.append(pair[0])
        arr.sort()

        left=0
        right=1
        ans=0
        while right<len(arr):
            diff=arr[right]-arr[left]
            ans=max(ans,diff)
            left+=1
            right+=1

        return ans
