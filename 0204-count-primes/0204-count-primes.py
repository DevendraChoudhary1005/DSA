class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        arr = [True]*n
        arr[0] = False
        arr[1] = False

        for i in range(2, int(n**0.5) + 1):
            if arr[i]:
                arr[i*i : n : i] = [False] * len(range(i*i, n, i))

        return sum(arr)