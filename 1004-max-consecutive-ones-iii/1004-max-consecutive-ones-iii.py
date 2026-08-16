class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """ Brute Force (TLE)
        max_len = 0
        n = len(nums)

        for i in range(0, n):
            zeros = 0 
            for j in range(i, n):
                if nums[j] == 0:
                    zeros += 1
                if zeros > k:
                    break
                max_len = max(max_len, j-i+1)

        return max_len"""

        max_len = 0
        n = len(nums)
        l = 0
        r = 0
        zeros = 0

        while r < n:
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                max_len = max(max_len, r-l+1)
            r += 1
        return max_len