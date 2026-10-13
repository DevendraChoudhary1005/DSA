class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Compute squares and sort them in ascending order
        squares = [x * x for x in nums]
        squares.sort()
        
        n = len(squares)
        m = n // 2  # Number of negative positions (odd indices)
        
        # Subtract the sum of the smallest m squares, add the rest
        return sum(squares[m:]) - sum(squares[:m])