class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_len = 1
        inc_count = 1
        dec_count = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                inc_count += 1
            else:
                inc_count = 1

            if nums[i] > nums[i+1]:
                dec_count += 1
            else:
                dec_count = 1

            max_len = max(inc_count, dec_count, max_len)

        return max_len

        

