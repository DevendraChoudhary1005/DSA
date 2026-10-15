class Solution:
    def maxSumOfSquares(self, num: int, sum_val: int) -> str:
        if sum_val < 0 or sum_val > 9 * num:
            return ""

        result = []
        for i in range(num):
            if sum_val >= 9:
                result.append('9')
                sum_val -= 9
            else:
                result.append(str(sum_val))
                sum_val = 0
            
        return "".join(result)     