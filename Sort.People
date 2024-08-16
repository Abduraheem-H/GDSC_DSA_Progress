


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hash_table = {}
        for i in range(len(heights)):
            hash_table[heights[i]] = names[i]
        heights.sort(reverse=True)
        for i in range(len(heights)):
            names[i] = hash_table[heights[i]]
        return names
#print(Solution.sortPeople(["Mary", "John", "Emma"], [180, 175, 170]))
