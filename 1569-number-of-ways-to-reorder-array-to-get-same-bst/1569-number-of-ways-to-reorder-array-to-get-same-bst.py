class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Precompute binomial coefficients using Pascal's triangle
        c = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if j == 0 or j == i:
                    c[i][j] = 1
                else:
                    c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD
                    
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            l_ways = dfs(left)
            r_ways = dfs(right)
            
            # Choose positions for the left subtree elements among total left+right slots
            comb = c[len(left) + len(right)][len(left)]
            
            return (comb * l_ways % MOD) * r_ways % MOD

        # Subtract 1 to exclude the original array ordering itself
        return (dfs(nums) - 1 + MOD) % MOD      