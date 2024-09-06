class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count = 0
        length = 0
        
        counter = Counter()
        
        for right in range(len(s)):
            counter[s[right]] += 1
            max_count = max(max_count, counter[s[right]])
            
            if (right - left + 1) - max_count > k:
                counter[s[left]] -= 1
                left += 1
            
            length = max(length, right - left + 1)
        
        return length



        