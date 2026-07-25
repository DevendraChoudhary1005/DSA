class Solution:
    def maxProduct(self, n: int) -> int:
        n_list = [int(x) for x in str(n)]
        n_list.sort()

        return n_list[-1]*n_list[-2]