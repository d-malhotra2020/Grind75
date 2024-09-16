class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append([r, c])
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    row = r + dr
                    col = c + dc
                    if (row < 0 or col < 0 or row == rows or col == columns or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -=1
            time +=1
        return time if fresh == 0 else -1