class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        columns = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= columns or grid[r][c] != '1':
                return

            grid[r][c] = '0'
            if r + 1 < rows:
                dfs(r + 1, c)
            if r >= 1:
                dfs(r - 1, c)
            if c + 1 < columns:
                dfs(r, c + 1)
            if c >= 1:
                dfs(r, c - 1)
    
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        return islands
