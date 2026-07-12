class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(list(set(arr)))

        rank_map = {}
        current = 1

        for num in sorted_arr:
            rank_map[num] = current
            current += 1

        return [rank_map[num] for num in arr]