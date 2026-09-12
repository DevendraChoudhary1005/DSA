from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        indexed_intervals = [
            (start, end, weight, i) 
            for i, (start, end, weight) in enumerate(intervals)
        ]
        
        indexed_intervals.sort(key=lambda x: x[1])
        
        n = len(intervals)
        end_times = [iv[1] for iv in indexed_intervals]
        
        def is_better(cand, current):
            w1, idxs1 = cand
            w2, idxs2 = current
            if w1 != w2:
                return w1 > w2
            return idxs1 < idxs2  
        
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            start, end, weight, orig_idx = indexed_intervals[i - 1]
            
            p = bisect_right(end_times, start - 1)
            
            for k in range(1, 5):
                best = dp[i - 1][k]
                prev_weight, prev_indices = dp[p][k - 1]
                new_indices = tuple(sorted(prev_indices + (orig_idx,)))
                cand = (prev_weight + weight, new_indices)
                
                if is_better(cand, best):
                    best = cand
                
                dp[i][k] = best

        ans = (0, ())
        for k in range(1, 5):
            if is_better(dp[n][k], ans):
                ans = dp[n][k]
                
        return list(ans[1])