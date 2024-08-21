class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        deck.sort(reverse=True)
        for i in range(len(deck)):
            if queue:
                queue.appendleft(queue.pop())
                
        
            queue.appendleft(deck[i])
        return list(queue)
#print(Solution.deckRevealedIncreasing(Solution, [17, 13, 11, 2, 3, 5, 7]))