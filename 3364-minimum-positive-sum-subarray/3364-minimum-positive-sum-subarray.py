class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        n = len(nums)

        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                length = j-i+1
                current_sum += nums[j]

                if l <= length <= r:
                    if current_sum > 0:
                        min_sum = min(min_sum, current_sum)
                elif length > r:
                    break
                
        return min_sum if min_sum != float('inf') else -1