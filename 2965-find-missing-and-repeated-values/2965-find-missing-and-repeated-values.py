class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = {}
        n = len(grid)
        for rows in grid:
            for i in rows:
                count[i] = count.get(i, 0)+1
        
        repeated = -1
        missing = -1

        for i in range(1, n*n+1):
            if count.get(i, 0) == 2:
                repeated = i
            elif count.get(i, 0) == 0:
                missing = i

        return [repeated, missing]

        