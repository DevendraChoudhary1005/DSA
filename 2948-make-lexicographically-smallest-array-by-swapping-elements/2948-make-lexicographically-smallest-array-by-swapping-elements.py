class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        pairs = [(nums[i], i) for i in range(n)]
        pairs.sort(key=lambda x: x[0])
        
        result = [0] * n
        
        i = 0
        while i < n:
            j = i + 1
            while j < n and pairs[j][0] - pairs[j-1][0] <= limit:
                j += 1
            
            group = pairs[i:j]
            
            indices = [p[1] for p in group]
            indices.sort()
            
            for k in range(len(indices)):
                result[indices[k]] = group[k][0]
        
            i = j
            
        return result