class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        columns = len(grid[0])
        visit = set()
        islands = 0
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visit:
                    self.dfs(grid, r, c)
                    islands +=1
        return islands
                    
                    
    def dfs(self, grid, r, c):
        rows = len(grid)
        columns = len(grid[0])
        
        if r < 0 or c < 0 or r >= rows or c >= columns or grid[r][c] != "1":
            return
        grid[r][c] = "#"
        self.dfs(grid, r+1, c)
        self.dfs(grid, r-1, c)
        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)
        