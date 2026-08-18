from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == n:
            return max(nums)

        count = Counter(nums)

        if k == 1:
            res = -1
            for num, count in count.items():
                if count == 1:
                    res = max(res, num)

            return res

        res = -1

        if count[nums[0]] == 1:
            res = max(res, nums[0])
        if count[nums[-1]] == 1:
            res = max(res, nums[-1])

        return res