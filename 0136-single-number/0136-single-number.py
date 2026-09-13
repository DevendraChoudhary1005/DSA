class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)

        result = min(counts, key = counts.get)

        return result