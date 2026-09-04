class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)

        for r in range(m):
            for c in range(n):
                diagonals[r - c].append(mat[r][c])

        for key in diagonals:
            diagonals[key].sort(reverse = True)

        for r in range(m):
            for c in range(n):
                mat[r][c] = diagonals[r-c].pop()

        return mat