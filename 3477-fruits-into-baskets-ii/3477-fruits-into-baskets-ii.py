class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False] * n
        unplaced_count = n

        for fruit in fruits:
            for j in range(n):
                if not used[j] and baskets[j] >= fruit:
                    used[j] = True
                    unplaced_count -= 1
                    break

        return unplaced_count