class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        mid = 1
        right = 2

        if len(nums)<2:
            return len(nums)

        while right < len(nums):
            if nums[left] == nums[mid] == nums[right]:
                nums.pop(right)
            else:
                left += 1
                mid += 1
                right += 1

        return len(nums)