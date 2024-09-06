


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        print(costs)
        count = 0
        sum = 0
        if coins < costs[0]:
            return 0
        for i in range(len(costs)):
            sum += costs[i]
            # print(sum)
            if sum > coins:
                break

            count += 1
        return count


#print(Solution.maxIceCream(Solution, [1, 6, 3, 1, 2, 5], 20))

        