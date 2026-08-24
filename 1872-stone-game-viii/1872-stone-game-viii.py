class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        prefix = [0]*n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i-1] + stones[i]

        best_score = prefix[-1]

        for i in range(n-2, 0, -1):
            best_score = max(best_score, prefix[i] - best_score)

        return best_score
