from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = rStart, cStart
        d = 0
        steps = 1
        count = 0
        
        while count < rows * cols:
            for _ in range(2):
                for _ in range(steps):
                    if 0 <= x < rows and 0 <= y < cols:
                        result.append([x, y])
                        count += 1
                    if count >= rows * cols:
                        return result
                    x += directions[d][0]
                    y += directions[d][1]
                d = (d + 1) % 4
            steps += 1

        return result



