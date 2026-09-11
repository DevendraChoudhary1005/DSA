from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh_count = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        minutes = 0
        
        while queue and fresh_count > 0:
            minutes += 1
            
            for _ in range(len(queue)):
                i, j = queue.popleft()
                
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_i, new_j = i + dx, j + dy
                    
                    if 0 <= new_i < rows and 0 <= new_j < cols:
                        if grid[new_i][new_j] == 1:
                            grid[new_i][new_j] = 2
                            fresh_count -= 1
                            queue.append((new_i, new_j))

        return minutes if fresh_count == 0 else -1
