class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        # Precompute divisors of n efficiently
        divisors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
            i += 1
            
        total_sum = 0
        
        for k in divisors:
            # Step 1: Check inter-block ordering (max of block i <= min of block i+1)
            block_maxes = []
            block_mins = []
            for start in range(0, n, k):
                b_max = nums[start]
                b_min = nums[start]
                for j in range(start + 1, start + k):
                    val = nums[j]
                    if val > b_max:
                        b_max = val
                    if val < b_min:
                        b_min = val
                block_maxes.append(b_max)
                block_mins.append(b_min)
                
            inter_valid = True
            for b in range(len(block_maxes) - 1):
                if block_maxes[b] > block_mins[b+1]:
                    inter_valid = False
                    break
            if not inter_valid:
                continue
                
            # Step 2: Check intra-block sortability via multisets and circular descents
            is_valid = True
            for start in range(0, n, k):
                block = nums[start:start+k]
                target = sorted_nums[start:start+k]
                
                # Verify multiset match
                if sorted(block) != target:
                    is_valid = False
                    break
                
                # Verify circular descents <= 1
                descents = 0
                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        descents += 1
                if descents > 1:
                    is_valid = False
                    break
                    
            if is_valid:
                total_sum += k
                
        return total_sum