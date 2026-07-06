class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        n = len(intervals)
        if n <= 1:
            return n
        
        remaining = n 
        current_interval = intervals[0]

        for i in range(1, n):
            next_interval = intervals[i]

            if next_interval[1] <= current_interval[1]:
                remaining -= 1
            else:
                current_interval = next_interval
                
        return remaining