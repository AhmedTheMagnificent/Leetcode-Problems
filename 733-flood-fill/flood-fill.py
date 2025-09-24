class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        colr = image[sr][sc]
        if colr == color:  # prevent infinite loop
            return image
        r, c = len(image), len(image[0])
        def dfs(i, j):
            if (i < 0 or i > r - 1) or (j < 0 or j > c - 1):
                return 
            if image[i][j] != colr:
                return 
            if image[i][j] == colr:
                image[i][j] = color
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        dfs(sr, sc)
        return image
