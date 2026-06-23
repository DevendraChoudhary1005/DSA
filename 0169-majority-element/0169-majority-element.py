class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] +=1

        n = len(nums)
        for key in count:
            if count[key]>n//2:
                return key