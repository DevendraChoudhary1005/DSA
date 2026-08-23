class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n//2

        sum_diff = 0
        mark_diff = 0

        for i in range(mid):
            if num[i] == '?':
                mark_diff += 1
            else:
                sum_diff += int(num[i])

        for i in range(mid, n):
            if num[i] == '?':
                mark_diff -= 1
            else:
                sum_diff -= int(num[i])

        if mark_diff % 2 != 0:
            return True

        return sum_diff + (mark_diff // 2) * 9 != 0 