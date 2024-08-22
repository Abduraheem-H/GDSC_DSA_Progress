class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left=0
        right=3
        count=0
        while right<=len(s):
            if len(set(s[left:right]))==3:
                count+=1
            left+=1
            right+=1
        return count



        