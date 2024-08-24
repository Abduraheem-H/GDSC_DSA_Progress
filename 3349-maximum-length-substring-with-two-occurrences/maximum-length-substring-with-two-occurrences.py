class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        length = 2
        right = 1
        while right <= len(s):
            hash_table = Counter(s[left:right])
            if max(hash_table.values()) <= 2:
                length = max(length, len(s[left:right]))
                right += 1
            else:
                left += 1
        return length
#print(Solution.maximumLengthSubstring(Solution, "aabb"))