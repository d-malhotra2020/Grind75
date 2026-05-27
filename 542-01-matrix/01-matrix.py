class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        columns = len(mat[0])
        queue = deque()
        result = [[-1] * columns for i in range(rows)]

        for r in range(rows):
            for c in range(columns):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    result[r][c] = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        distance = 1
        while queue:
            level = len(queue)
            for i in range(level):
                currentX, currentY = queue.popleft()
                for directionX, directionY in directions:
                    newX = currentX + directionX
                    newY = currentY + directionY

                    if 0 <= newX < rows and 0 <= newY < columns:
                        if result[newX][newY] == -1:
                            result[newX][newY] = distance
                            queue.append((newX, newY))
            distance += 1
        return result
                    

