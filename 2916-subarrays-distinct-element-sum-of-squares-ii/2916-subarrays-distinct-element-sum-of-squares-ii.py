class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Pack count (upper bits) and sum of indices (lower bits) into a single integer
        SHIFT = 40
        MASK = (1 << SHIFT) - 1
        
        bit = [0] * (n + 1)
        
        def add(idx, val):
            i = idx + 1
            while i <= n:
                bit[i] += val
                i += i & (-i)
                
        def query(idx):
            i = idx + 1
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & (-i)
            return res

        last = {}
        totC = 0
        totS = 0
        g = 0
        ans = 0
        
        for j in range(n):
            v = nums[j]
            p = last.get(v, -1)
            
            if p >= 0:
                # Remove previous occurrence from BIT
                add(p, -((1 << SHIFT) + p))
                totC -= 1
                totS -= p
                
                # Query BIT for elements in the range [p+1, j-1]
                q_res = query(j - 1) - query(p)
                cSuf = q_res >> SHIFT
                sSuf = q_res & MASK
                R = sSuf - p * cSuf
            else:
                R = totS + totC
                
            g = (g + 2 * R + (j - p)) % MOD
            ans = (ans + g) % MOD
            
            # Add current occurrence to BIT
            add(j, (1 << SHIFT) + j)
            totC += 1
            totS += j
            last[v] = j
            
        return ans