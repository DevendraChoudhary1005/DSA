class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    perimeter += 4

                    if i>0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j>0 and grid[i][j-1] == 1:
                        perimeter -= 2

        return perimeter 