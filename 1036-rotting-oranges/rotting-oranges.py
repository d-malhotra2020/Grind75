class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()
        oranges = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    oranges += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0
        while queue and oranges > 0:
            levels = len(queue)
            minutes += 1
            for i in range(levels):
                currentX, currentY = queue.popleft()
                for directionX, directionY in directions:
                    newX = currentX + directionX
                    newY = currentY + directionY
                    if 0 <= newX < rows and 0 <= newY < columns and grid[newX][newY] == 1:
                        grid[newX][newY] = 2
                        queue.append((newX, newY))
                        oranges -= 1
        return minutes if oranges == 0 else -1

                
