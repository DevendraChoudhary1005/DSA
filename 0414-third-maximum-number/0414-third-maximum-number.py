class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = sorted(set(nums))

        if len(unique_nums) < 3:
            return unique_nums[-1]
        
        return unique_nums[-3]
        