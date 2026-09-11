class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        target = 1

        for x in nums:
            if x == target:
                target += 1

        return target
