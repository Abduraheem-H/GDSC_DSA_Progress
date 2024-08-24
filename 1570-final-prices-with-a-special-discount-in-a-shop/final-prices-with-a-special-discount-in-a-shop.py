class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = [p for p in prices]
        stack = []

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                discount = stack.pop()
                result[discount] -= price

            stack.append(i)

        return result
