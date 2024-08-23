class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n

        if k == 0:
            return result

        for i in range(n):
            if k > 0:
                left = (i + 1) % n
                right = (i + k) % n
                if left <= right:
                    sumi = sum(code[left:right + 1])
                else:
                    sumi = sum(code[left:]) + sum(code[:right + 1])
            else:
                left = (i + k) % n
                right = (i - 1 + n) % n
                if left <= right:
                    sumi = sum(code[left:right + 1])
                else:
                    sumi = sum(code[left:]) + sum(code[:right + 1])

            result[i] = sumi

        return result
