class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Count the frequency of each bit across all numbers
        bits = [0] * 32
        for x in nums:
            for i in range(32):
                if (x >> i) & 1:
                    bits[i] += 1
                    
        # Reconstruct numbers by placing set bits into the most significant positions first
        n = len(nums)
        arr = [0] * n
        for i in range(32):
            count = bits[i]
            for j in range(count):
                arr[j] |= (1 << i)
                
        # Sort in descending order to prioritize the largest numbers
        arr.sort(reverse=True)
        
        # Calculate the sum of squares of the top k elements modulo 10^9 + 7
        ans = 0
        for i in range(k):
            ans = (ans + arr[i] * arr[i]) % MOD
            
        return ans