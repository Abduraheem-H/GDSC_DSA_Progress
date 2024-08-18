


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        new_list=[]
        sum=0
        left = 0 
        right = len(skill)-1
        chemy= skill[left] + skill[right]
        while left < right:
            if skill[left] + skill[right] ==chemy:
                new_list.append((skill[left], skill[right]))
                left+=1
                right-=1

            else:
                return -1
        for pair in new_list:
            sum+=(pair[0]*pair[1])
        print(new_list)
        return sum
#print(Solution.dividePlayers([1,1]))
