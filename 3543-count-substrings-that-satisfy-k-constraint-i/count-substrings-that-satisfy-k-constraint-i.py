class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        
        length = len(s)
        count = len(s)
        for i in range(length):
            for j in range(i + 2, length + 1):
                substring = s[i:j]
                if substring.count("0") <= k or substring.count("1") <= k:
                    count += 1
        return count


