class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        special_sum = 0
        n = len(nums)

        for i in range(n):
            if n % (i+1) == 0:
                special_sum += nums[i]*nums[i]

        return special_sum