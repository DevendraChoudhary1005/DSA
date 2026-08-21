import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # OPTIMIZATION 1: Remove redundant coins to shrink 'n'
        coins.sort()
        filtered_coins = []
        for c in coins:
            # Only keep the coin if it's not a multiple of any smaller coin we already kept
            if not any(c % fc == 0 for fc in filtered_coins):
                filtered_coins.append(c)
        coins = filtered_coins
        n = len(coins)
        
        # Determine the absolute maximum bound
        max_bound = coins[0] * k
        
        # OPTIMIZATION 3: Separate lists to remove the 'if' statement from the binary search
        add_lcms = []
        sub_lcms = []

        for i in range(1, 1 << n):
            curr_lcm = 1
            set_bits = 0

            for j in range(n):
                if (i >> j) & 1:
                    curr_lcm = math.lcm(curr_lcm, coins[j])
                    set_bits += 1
            
            # OPTIMIZATION 2: Only save LCMs that are strictly useful
            if curr_lcm <= max_bound:
                if set_bits % 2 == 1:
                    add_lcms.append(curr_lcm)
                else:
                    sub_lcms.append(curr_lcm)

        def count_multiples(x):
            count = 0
            # Execute without evaluating any conditions
            for lcm_val in add_lcms:
                count += x // lcm_val
            for lcm_val in sub_lcms:
                count -= x // lcm_val
            return count

        left = 1
        right = max_bound

        while left < right:
            mid = (left + right) // 2

            if count_multiples(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left