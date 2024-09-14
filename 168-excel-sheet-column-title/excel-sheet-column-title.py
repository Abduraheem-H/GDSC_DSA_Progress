class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        val = columnNumber
        ans = []
        while val > 0:
            val -= 1
            rem = int(val % 26)
            ans.append(chr(rem + 65))
            val //= 26
        ans.reverse()

        return "".join(ans)


#print(Solution.convertToTitle(Solution, 701))

        