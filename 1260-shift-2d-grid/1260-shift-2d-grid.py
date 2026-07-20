class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        total_elements = m*n
        k = k % total_elements

        result  = [[0]*n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                current_1d = r * n + c

                new_1d = (current_1d + k) % total_elements

                new_r = new_1d // n
                new_c = new_1d % n

                result[new_r][new_c] = grid[r][c]

        return result