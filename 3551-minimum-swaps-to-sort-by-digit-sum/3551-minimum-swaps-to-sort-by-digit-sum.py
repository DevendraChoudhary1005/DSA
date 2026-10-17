class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        
        # Create the sorted target arrangement: (digit_sum, value)
        sorted_nums = sorted(nums, key=lambda x: (get_digit_sum(x), x))
        
        # Map each value to its target index in the sorted array
        num_to_index = {val: i for i, val in enumerate(sorted_nums)}
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If already visited or already in the correct position, skip
            if visited[i] or num_to_index[nums[i]] == i:
                continue
                
            # Traverse the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = num_to_index[nums[curr]]
                cycle_size += 1
                
            # Add swaps needed for this cycle
            if cycle_size > 1:
                swaps += cycle_size - 1
                
        return swaps     