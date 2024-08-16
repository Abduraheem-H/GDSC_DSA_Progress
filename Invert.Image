class Solution:
    def flipAndInvertImage( self, image: List[List[int]]) -> List[List[int]]:
        counter = 0
        for row in image:

            left=0
            right=len(row)-1
            while left<right:
                row[left], row[right] = row[right], row[left]
                left+=1
                right-=1
                if left==right:
                    continue
            for i in range(len(row)):
                if row[i]==0:
                    row[i] =1
                else:
                    row[i] =0
            image[counter] =row
            counter+=1
        return image
#print(Solution.flipAndInvertImage([[1, 1], [0, 0]]))
