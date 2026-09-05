class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        if n <= 1:
            return 0

        max_nums = [nums[0]]*n
        min_nums = [nums[-1]]*n

        for i in range(n-2, -1, -1):
            min_nums[i] = min(min_nums[i+1], nums[i])

        for i in range(1, n):
            max_nums[i] = max(max_nums[i-1], nums[i])

        for i in range(n):
            if max_nums[i] - min_nums[i] <= k:
                return i

        return -1
