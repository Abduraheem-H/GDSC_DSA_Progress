class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left=0
        right= 0
        result=[]
        if not firstList or not secondList:
            return result
        while left< len(firstList) and right< len(secondList):
            a= max(firstList[left][0], secondList[right][0])
            b= min(firstList[left][1], secondList[right][1])
            if a<=b:
                result.append([a,b])
            if firstList[left][1]<secondList[right][1]:
                left+=1
            elif firstList[left][1]>secondList[right][1]:
                right+=1
            else:
                left+=1
                right+=1
        return result
# print(
#     Solution.intervalIntersection(
#         Solution,
#         [[]],
#         [[1, 5], [8, 12], [15, 24], [25, 26],[27,28]],
#     )
# )
