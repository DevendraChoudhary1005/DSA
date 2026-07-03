class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        
        def solve(index, total, subset):
            if total == target:
                result.append(subset.copy())
                return
            elif total > target:
                return
            if index >= len(candidates):
                return

            new_total = total + candidates[index]
            subset.append(candidates[index])
            
            solve(index, new_total, subset)
            
            subset.pop()
            solve(index + 1, total, subset)

        solve(0, 0, [])
        return result