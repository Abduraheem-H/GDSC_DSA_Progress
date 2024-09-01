class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        counter = 0
        fruit_count = Counter()
        
        for right in range(len(fruits)):
            fruit_count[fruits[right]] += 1
            
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1
            
            counter = max(counter, right - left + 1)
        
        return counter
