class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def solve(index, target, subset, curr_sum):
            if curr_sum == target:
                result.append(subset.copy())
                return
            elif curr_sum > target:
                return
            
            for i in range(index, len(nums)):
                if i>index and nums[i] == nums[i-1]:
                    continue

                subset.append(nums[i])
                solve(i+1, target, subset, curr_sum+nums[i])
                subset.pop()

        solve(0, target, [], 0)

        return result