from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0

        thief_queue = deque()
        dist_to_thief = [[-1] * n for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    thief_queue.append((r, c))
                    dist_to_thief[r][c] = 0
                    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while thief_queue:
            r, c = thief_queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist_to_thief[nr][nc] == -1:
                    dist_to_thief[nr][nc] = dist_to_thief[r][c] + 1
                    thief_queue.append((nr, nc))

        def has_valid_path(safeness: int) -> bool:
            if dist_to_thief[0][0] < safeness or dist_to_thief[n-1][n-1] < safeness:
                return False
                
            q = deque([(0, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            
            while q:
                r, c = q.popleft()
                if r == n - 1 and c == n - 1:
                    return True
                    
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    
                        if dist_to_thief[nr][nc] >= safeness:
                            visited[nr][nc] = True
                            q.append((nr, nc))
            return False

        low, high = 0, 2 * n
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            if has_valid_path(mid):
                result = mid   
                low = mid + 1
            else:
                high = mid - 1  
                
        return result