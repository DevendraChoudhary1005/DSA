class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n

        def reverse(nums, left, right):
            while left<right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(nums, n-k, n-1)
        reverse(nums, 0, n-k-1)
        reverse(nums, 0, n-1)

        