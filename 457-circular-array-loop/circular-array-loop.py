class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            right, left = i, i
            while nums[right] * nums[next_index(left)] > 0 and nums[right] * nums[next_index(next_index(left))] > 0:
                right = next_index(right)
                left = next_index(next_index(left))
                if right == left:
                    if right == next_index(left):  
                        break
                    return True

            right = i
            while nums[right] * nums[next_index(right)] > 0:
                tmp = right
                right = next_index(right)
                nums[tmp] = 0

        return False

