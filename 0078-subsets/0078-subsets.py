class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """result = []
        n = len(nums)
        total_subsets = 1<<n

        for num in range(0, total_subsets):
            lst = []
            for i in range(0, n):
                if num & (1<<i) != 0:
                    lst.append(nums[i])

            result.append(lst)

        return result"""
        result = []

        def gen_subsets(index, subset):
            if index >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[index])
            gen_subsets(index+1, subset)
            subset.pop()
            gen_subsets(index+1, subset)

        gen_subsets(0, [])

        return result