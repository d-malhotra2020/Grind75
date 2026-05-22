class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        rows = len(image)
        columns = len(image[0])

        if original == color:
            return image

        def dfs(r, c):
            if image[r][c] != original:
                return 
            image[r][c] = color

            if r + 1 < rows:
                dfs(r + 1, c)
            if r >= 1:
                dfs(r - 1, c)
            if c + 1 < columns:
                dfs(r, c + 1)
            if c >= 1:
                dfs(r, c - 1)
        
        dfs(sr, sc)
        return image