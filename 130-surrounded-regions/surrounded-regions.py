class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        columns = len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= columns or board[r][c] != 'O':
                return
            board[r][c] = "S"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for i in range(rows):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][columns - 1] == "O":
                dfs(i, columns - 1)
        for j in range(columns):
            if board[0][j] == "O":
                dfs(0, j)
            if board[rows - 1][j] == "O":
                dfs(rows - 1, j)
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return board

        