class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        digit = len(columnTitle) - 1
        sum = 0
        for letter in columnTitle:
            value = (ord(letter) - 65) + 1
            sum += value * (26**digit)
            digit -= 1
        return sum


#print(Solution.titleToNumber(Solution, "ZY"))



        