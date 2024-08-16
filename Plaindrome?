class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringList = []
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                stringList.append(s[i].lower())

            else:
                continue
       
        left = 0
        right = len(stringList) - 1
        while left<right:
            if stringList[left] != stringList[right]:
                return False
            else:
                left += 1
                right -= 1
            
        return True
   
