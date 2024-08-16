class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            x, y = point
            distance = math.sqrt(x**2 + y**2)
            distances.append((distance, point))
    
        distances.sort()
    
        return [point for distance, point in distances[:k]]
