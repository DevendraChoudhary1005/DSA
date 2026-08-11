class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        prefix_sum = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                prefix_sum += nums[i + 1]
            else:
                break
        
        num_set = set(nums)
        
        while prefix_sum in num_set:
            prefix_sum += 1
            
        return prefix_sum


         
        