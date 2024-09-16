class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        q = deque([(0, 0, 1)])
        visit = set((0, 0))
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        
        while q:
            r, c, length = q.popleft()
            if r < 0 or c < 0 or r >= rows or c >= rows or grid[r][c] == 1:
                continue
            if (r == rows - 1 and c == rows -1):
                return length
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if (row, col) not in visit:
                    q.append((row, col, length+1))
                    visit.add((row, col))
        return -1