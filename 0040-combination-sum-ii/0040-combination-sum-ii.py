class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def backTrack(index, total, subset):
            if total == 0:
                result.append(subset.copy())
                return
            if total<0 or index>=len(nums):
                return

            for i in range(index, len(nums)):
                if i>index and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backTrack(i+1, total-nums[i], subset)
                subset.pop()

        backTrack(0, target, [])
        return result