class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1:
            return 0
        
        
        parent=self.kthGrammar(n-1,(k//2)+(k%2))

        isKth=k%2
        if parent ==0:
            if isKth==1:
                return 0
            else:
                return 1
        else:
            if isKth==1:
                return 1
            else:
                return 0
        
        
     
