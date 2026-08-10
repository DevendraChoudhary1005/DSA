class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        duplicate = -1
        missing = -1

        if nums[0] != 1:
            missing = 1

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                duplicate = nums[i]

            elif nums[i+1] - nums[i]>1:
                if missing == -1:
                    missing = nums[i]+1

        if nums[-1] != n and missing == -1:
            missing = n

        return [duplicate, missing]
        