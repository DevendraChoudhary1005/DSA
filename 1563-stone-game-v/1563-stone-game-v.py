class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        
        # dp[i][j] stores the max score for interval [i, j]
        dp = [[0] * n for _ in range(n)]
        
        # max_l[i][j] stores max(dp[i][k] + sum(i..k)) for k from i to j
        max_l = [[0] * n for _ in range(n)]
        
        # max_r[i][j] stores max(dp[k][j] + sum(k..j)) for k from i to j
        max_r = [[0] * n for _ in range(n)]
        
        # Base cases: intervals of length 1
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]
            
        # Build the DP table bottom-up
        for i in range(n - 1, -1, -1):
            total_sum = stoneValue[i]
            left_sum = 0
            mid = i - 1  # 'mid' is the largest index where left_sum <= right_sum
            
            for j in range(i + 1, n):
                total_sum += stoneValue[j]
                
                # Advance mid until left_sum is about to exceed right_sum
                # Since total_sum = left_sum + right_sum, left_sum <= right_sum is equivalent to left_sum * 2 <= total_sum
                while mid + 1 < j and (left_sum + stoneValue[mid + 1]) * 2 <= total_sum:
                    mid += 1
                    left_sum += stoneValue[mid]
                    
                res = 0
                
                # Option 1: Valid split points where left_sum <= right_sum
                if mid >= i:
                    if left_sum * 2 == total_sum:
                        # If perfectly equal, Alice can choose either the best left-side play or best right-side play
                        res = max(max_l[i][mid], max_r[mid + 1][j])
                    else:
                        # Left side is strictly smaller
                        res = max_l[i][mid]
                        # Right side becomes strictly smaller AFTER the mid point
                        if mid + 2 <= j:
                            res = max(res, max_r[mid + 2][j])
                            
                # Option 2: If no mid point exists, the right side is ALWAYS smaller
                else:
                    res = max_r[i + 1][j]
                    
                dp[i][j] = res
                
                # Update our rolling maximums for future larger intervals
                max_l[i][j] = max(max_l[i][j - 1], dp[i][j] + total_sum)
                max_r[i][j] = max(max_r[i + 1][j], dp[i][j] + total_sum)
                
        return dp[0][n - 1]