from collections import Counter
from itertools import accumulate
import bisect

class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_val = max(nums)
        
        freq = Counter(nums)
        gcd_pair_counts = [0] * (max_val + 1)
        
        for i in range(max_val, 0, -1):
            multiples = sum(freq[j] for j in range(i, max_val + 1, i))
            
            total_pairs = multiples * (multiples - 1) // 2
            
            excess_pairs = sum(gcd_pair_counts[j] for j in range(2 * i, max_val + 1, i))
            
            gcd_pair_counts[i] = total_pairs - excess_pairs
            
        prefix_sums = list(accumulate(gcd_pair_counts))
        
        return [bisect.bisect_right(prefix_sums, q) for q in queries]
        