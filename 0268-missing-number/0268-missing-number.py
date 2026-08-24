class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        sum_of_n = (n*(n+1))//2

        for i in range(n):
            total += nums[i]

        return sum_of_n - total