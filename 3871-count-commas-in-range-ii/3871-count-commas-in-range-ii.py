class Solution:
    def countCommas(self, n: int) -> int:
        total_comas = 0
        threshold = 1000

        while threshold <= n:
            total_comas += (n-threshold+1)
            threshold *= 1000

        return total_comas
        
        