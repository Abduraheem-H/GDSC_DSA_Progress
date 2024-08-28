class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        
        total_turns = min(x, y // 4)
        
        
        if total_turns % 2 == 1:
            return "Alice"
        else:
            return "Bob"
