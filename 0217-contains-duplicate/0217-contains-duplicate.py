class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()

        for i in range(len(nums)):
            if nums[i] in my_set:
                return True
            my_set.add(nums[i])

        return False
        