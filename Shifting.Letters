
class Solution:
    def shiftingLetters(self,s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        string = [ord(x) for x in s]
        base = [0] * (n + 1)  
        
        for left, right, direction in shifts:
            if direction == 1:
                base[left] += 1
                if right + 1 < n:
                    base[right + 1] -= 1
            else:
                base[left] -= 1
                if right + 1 < n:
                    base[right + 1] += 1

        
        for i in range(1, n):
            base[i] += base[i - 1]

        
        for i in range(n):
            string[i] += base[i]
            while string[i] < 97:
                string[i] += 26
            while string[i] > 122:
                string[i] -= 26

        
        return "".join(chr(char) for char in string)



# print(
#     Solution.shiftingLetters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]])
# )
