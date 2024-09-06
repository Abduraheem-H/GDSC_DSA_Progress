class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        #[1,2,3,4,5,6,7,8,9]
        #[1,2,2,4,7,8]
        piles.sort()
        mySum=0
        l=0
        m=len(piles)-2
        while m>l:
            mySum+=piles[m]
            m-=2
            l+=1
        return mySum
       
        