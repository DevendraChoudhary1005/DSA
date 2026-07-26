class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            num = nums[i]
            
            if num in window:
                return True

            window.add(num)

            if len(window) > k:
                window.remove(nums[i-k])

        return False