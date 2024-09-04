


class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = list(str(num))
        if num == 0:
            return num

        if nums[0] != "-":
            sorted_nums = sorted(nums)
            print(sorted_nums)
            for num in sorted_nums:
                if num != "0":
                    mini = sorted_nums.index(num)
                    break
            sorted_nums.insert(0, sorted_nums.pop(mini))

        else:
            nums.pop(0)
            sorted_nums = sorted(nums, reverse=True)

            sorted_nums.insert(0, "-")

        return int("".join(sorted_nums))


#print(Solution.smallestNumber(Solution, -7605))

#print(Solution.smallestNumber(Solution, -1432403))