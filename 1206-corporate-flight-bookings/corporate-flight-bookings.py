


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_sum=[0]*(n)
        
        for flight in bookings:
            prefix_sum[flight[0]-1] +=flight[2]
            if flight[1] < len(prefix_sum):
                prefix_sum[flight[1]] -=flight[2]
        
        for u in range(1,len(prefix_sum)):
            prefix_sum[u] +=prefix_sum[u-1]
        return prefix_sum

            

print(Solution.corpFlightBookings(Solution, [[1, 2, 10], [2, 3, 20], [2, 5, 25]],5))
