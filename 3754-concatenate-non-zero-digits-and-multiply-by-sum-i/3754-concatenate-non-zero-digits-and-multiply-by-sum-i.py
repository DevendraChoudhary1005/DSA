class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        
        digits = int(str(n).replace('0', '')or '0')
        digits_sum = sum(int(x) for x in str(n))

        return digits*digits_sum

