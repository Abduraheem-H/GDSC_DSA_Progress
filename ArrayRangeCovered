class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # [[2, 4], [6, 8], [10, 12]]
        hash_table={}
        counter=0
        for row in ranges:
            subArray=row
            for i in range(row[0],row[1]+1):
                hash_table[counter]=i
                counter+=1
        
        for i in range(left,right+1):
            
            if i not in hash_table.values():

                return False
        return True
#print(Solution.isCovered([[2, 4], [5, 8], [10, 12]],3,7))
