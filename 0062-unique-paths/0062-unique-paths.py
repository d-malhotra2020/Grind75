class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = [1] * n
        for i in range(m-1):
            newRows = [1] * n
            for j in range(n-2, -1 , -1):
                newRows[j] = newRows[j+1] + rows[j]
            rows = newRows
        return rows[0]