class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visit = set()
        
        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == columns or grid[r][c] == 0 or (r, c) in visit:
                return 0
            visit.add((r, c))
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))
        
        
        area = 0
        for r in range(rows):
            for c in range(columns):
                area = max(area, dfs(r, c))
                
        return area
                