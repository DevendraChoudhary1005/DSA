class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()

        while nums[-1]:
            nums[0], nums[-1] = nums[-1], nums[0]%nums[-1]

        return nums[0]