class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        deck.sort(reverse=True)
        for i in range(len(deck)):
            if queue:
                queue.append(queue.popleft())
                queue.append(deck[i])
            else:
                queue.append(deck[i])
        return [ i for i in reversed(queue)]
#print(Solution.deckRevealedIncreasing(Solution, [17, 13, 11, 2, 3, 5, 7]))