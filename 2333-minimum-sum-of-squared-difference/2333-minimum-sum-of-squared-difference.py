class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = [abs(nums1[i] - nums2[i]) for i in range(n)]
        total_k = k1 + k2

        if sum(diff) <= total_k:
            return 0

        left, right = 0, max(diff)
        optimal_max = right

        while left <= right:
            mid = (left + right) // 2

            operations_needed = sum(max(0, d-mid) for d in diff)

            if operations_needed <= total_k:
                optimal_max = mid
                right = mid - 1
            else:
                left = mid + 1

        remaining_k = total_k
        for i in range(n):
            if diff[i] > optimal_max:
                remaining_k -= (diff[i] - optimal_max)
                diff[i] = optimal_max

        for i in range(n):
            if remaining_k == 0:
                break
            if diff[i] == optimal_max and diff[i] > 0:
                diff[i] -= 1
                remaining_k -= 1

        return sum(d*d for d in diff) 