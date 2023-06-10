class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        visit = set()
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    visit.add((r, c))
                    queue.append((r,c))
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0),(0, 1), (0, -1)]:
                row, col = r+dr, c+dc
                if 0<= row<rows and 0<=col<cols and (row, col) not in visit:
                    mat[row][col] = mat[r][c]+1
                    visit.add((row,col))
                    queue.append((row,col))
        return mat
