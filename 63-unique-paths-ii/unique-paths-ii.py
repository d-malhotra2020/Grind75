class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])
        dp = [0] * columns
        dp[columns - 1] = 1
        
        for r in reversed(range(rows)):
            for c in reversed(range(columns)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c+1 < columns:
                    dp[c] = dp[c] + dp[c+1]
        return dp[0]