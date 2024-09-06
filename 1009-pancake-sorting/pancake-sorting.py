


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        left = 0
        right = len(arr) - 1

        while right > left:
            large = max(arr[: right + 1])

            idx = arr.index(large)
            if idx == 0:
                arr[: right + 1] = arr[: right + 1][::-1]
                ans.append(right + 1)
            else:
                arr[: idx + 1] = reversed(arr[: idx + 1])
                arr[: right + 1] = arr[: right + 1][::-1]
                print("rev", arr[: idx + 1])
                ans.append(idx + 1)
                ans.append(right + 1)
            right -= 1
        return ans


#print(Solution.pancakeSort(Solution, [3, 2, 4, 1]))
