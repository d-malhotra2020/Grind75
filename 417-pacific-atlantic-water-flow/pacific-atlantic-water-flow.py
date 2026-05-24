class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows = len(heights)
        columns = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, reachable):
            reachable.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < columns:
                    if (nr, nc) not in reachable and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, reachable)
        
        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, columns - 1, atlantic)
        
        for j in range(columns):
            dfs(0, j, pacific)
            dfs(rows - 1, j, atlantic)
        
        return list(pacific & atlantic)


                
