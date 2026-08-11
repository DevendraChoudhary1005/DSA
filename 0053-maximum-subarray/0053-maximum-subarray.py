class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        total = 0
        n = len(nums)

        for i in range(len(nums)):
            total = total + nums[i]

            if total>max_sum:
                max_sum = total
            if total < 0:
                total = 0

        return max_sum 