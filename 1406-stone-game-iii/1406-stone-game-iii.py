from functools import cache
from typing import List


class Solution:

  def stoneGameIII(self, stoneValue: List[int]) -> str:
    n = len(stoneValue)

    @cache
    def dp(i: int) -> int:
      if i >= n:
        return 0

      ans = float("-inf")
      current_stones = 0

      # Try taking 1, 2, or 3 stones
      for k in range(1, 4):
        if i + k - 1 < n:
          current_stones += stoneValue[i + k - 1]
          # Current player gains current_stones, but subtracts opponent's optimal gain
          ans = max(ans, current_stones - dp(i + k))

      return ans

    alice_diff = dp(0)

    if alice_diff > 0:
      return "Alice"
    elif alice_diff < 0:
      return "Bob"
    else:
      return "Tie"