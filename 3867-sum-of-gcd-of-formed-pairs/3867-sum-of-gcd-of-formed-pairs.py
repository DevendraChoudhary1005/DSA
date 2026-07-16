import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_gcd = []

        max_el = -1
        for x in nums:
            max_el = max(max_el, x)
            prefix_gcd.append(math.gcd(x, max_el))

        prefix_gcd.sort()

        total_sum = 0
        i, j = 0, n-1
        while i<j:
            total_sum += math.gcd(prefix_gcd[i], prefix_gcd[j])
            i += 1
            j -= 1

        return total_sum