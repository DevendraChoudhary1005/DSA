class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r>= m or c < 0 or c >= n or grid[r][c] == 1:
                return
            
            grid[r][c] = 1

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and grid[i][j] == 0:
                    dfs(i, j)

        closed_islands = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 0:
                    closed_islands += 1
                    dfs(i, j)
                
        return closed_islands