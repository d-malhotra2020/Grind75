class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        columns = len(grid[0])
        islands = 0


        def dfs(r, c):
            grid[r][c] = '0'
            if r + 1 < rows and grid[r +1][c] == '1':
                dfs(r + 1, c)
            if r >= 1 and grid[r - 1][c] == '1':
                dfs(r - 1, c)
            if c + 1 < columns and grid[r][c + 1] == '1':
                dfs(r, c + 1)
            if c >= 1 and grid[r][c - 1] == '1':
                dfs(r, c - 1)

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        return islands



