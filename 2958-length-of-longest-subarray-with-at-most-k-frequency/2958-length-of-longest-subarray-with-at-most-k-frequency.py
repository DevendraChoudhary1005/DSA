class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        max_len = 0

        for right in range(len(nums)):
            curr_num = nums[right]
            freq[curr_num] = freq.get(curr_num, 0) + 1

            while freq[curr_num] > k:
                left_num = nums[left]
                freq[left_num] -= 1
                left += 1

            max_len = max(max_len, right-left+1)

        return max_len