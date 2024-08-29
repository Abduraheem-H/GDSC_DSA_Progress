class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        result=n//3
        if n==1:
            return True
        elif(n%3==0):
            return self.isPowerOfThree(result)
        return False
        