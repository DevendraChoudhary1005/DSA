class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        max_sum = 0

        if n == k:
            return sum(cardPoints)

        left_sum = 0
        right_sum = 0

        for i in range(0, k):
            left_sum += cardPoints[i]

        max_sum = left_sum

        right = n-1

        for i in range(k-1, -1, -1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[right]

            max_sum = max(max_sum, left_sum+right_sum)
            right -= 1

        return max_sum