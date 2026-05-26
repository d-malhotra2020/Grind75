class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        queue = deque([(0, 0, 0)])
        visited = set((0, 0))

        while queue:
            currentX, currentY, moves = queue.popleft()

            if (currentX, currentY) == (x, y):
                return moves

            for directionX, directionY in directions:
                newX = currentX + directionX
                newY = currentY + directionY
                
                if (newX, newY) not in visited:
                    visited.add((newX, newY))
                    queue.append((newX, newY, moves + 1))
        return -1