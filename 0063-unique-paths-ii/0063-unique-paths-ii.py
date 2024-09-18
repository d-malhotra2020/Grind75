class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])
        dp = {(rows - 1, columns - 1): 1}
        
        def dfs(r, c):
            if r == rows or c == columns or obstacleGrid[r][c]:
                return 0
            if (r, c) in dp:
                    return dp[(r, c)]
            dp[(r, c)] = dfs(r+1, c)  + dfs(r, c+1)
            return dp[(r, c)]
        return dfs(0, 0)