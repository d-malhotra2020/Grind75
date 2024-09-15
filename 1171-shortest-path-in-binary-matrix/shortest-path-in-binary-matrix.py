class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        q = deque([(0, 0, 1)])
        visit = set((0, 0))
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        
        while q:
            r, c, length = q.popleft()
            if r < 0 or c < 0 or r >= rows or c >= rows or grid[r][c] == 1:
                continue
            if (r == rows - 1 and c == rows - 1):
                return length
            for dr, dc in direction:
                if (r + dr, c + dc) not in visit:
                    q.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))
        return -1