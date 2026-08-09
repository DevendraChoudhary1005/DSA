from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        total_sum = sum(piles)

        @lru_cache(maxsize=None)
        def dp(i: int, M: int) -> int:
            # Base case: no piles left
            if i >= n:
                return 0
            
            # If remaining piles are <= 2 * M, pick all remaining piles
            if n - i <= 2 * M:
                return sum(piles[i:])
            
            max_diff = float('-inf')
            current_piles_sum = 0
            
            # Try taking X piles where 1 <= X <= 2 * M
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break
                current_piles_sum += piles[i + X - 1]
                # Maximize (current player's gain - next player's gain)
                max_diff = max(max_diff, current_piles_sum - dp(i + X, max(M, X)))
                
            return max_diff

        alice_minus_bob = dp(0, 1)
        return (total_sum + alice_minus_bob) // 2