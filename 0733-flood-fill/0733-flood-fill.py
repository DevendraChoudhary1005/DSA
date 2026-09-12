class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_color = image[sr][sc]

        if initial_color == color:
            return image

        r = len(image)
        c = len(image[0])

        def dfs(i, j):
            if i<0 or i>=r or j<0 or j>=c:
                return

            if image[i][j] != initial_color:
                return

            image[i][j] = color

            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i, j-1)

        dfs(sr, sc)
        return image