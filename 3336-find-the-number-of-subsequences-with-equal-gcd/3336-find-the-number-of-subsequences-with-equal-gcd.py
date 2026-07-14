class Solution:
    def subsequencePairCount(self, nums) -> int:
        MOD = 10**9 + 7
        max_val = 200
        
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        dp = [[0] * (max_val + 1) for _ in range(max_val + 1)]
        
        dp[0][0] = 1
        
        for num in nums:
            next_dp = [row[:] for row in dp]
            
            for x in range(max_val + 1):
                for y in range(max_val + 1):
                    count = dp[x][y]
                    if count == 0:
                        continue
                    
                    g1 = num if x == 0 else gcd(x, num)
                    next_dp[g1][y] = (next_dp[g1][y] + count) % MOD
                    
                    g2 = num if y == 0 else gcd(y, num)
                    next_dp[x][g2] = (next_dp[x][g2] + count) % MOD
            
            dp = next_dp
            
        total_pairs = 0
        for i in range(1, max_val + 1):
            total_pairs = (total_pairs + dp[i][i]) % MOD
            
        return total_pairs