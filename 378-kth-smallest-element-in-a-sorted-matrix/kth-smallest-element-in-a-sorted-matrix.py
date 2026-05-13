class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def smallEqual(matrix, target):
            n = len(matrix)
            row = n - 1
            columns = 0
            count = 0

            while row >= 0 and columns < n:
                if matrix[row][columns] <= target:
                    count += row + 1
                    columns += 1
                else:
                    row -= 1
            return count >= k
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n - 1][n - 1]
        while left < right:
            mid = (left + right) // 2
            if smallEqual(matrix, mid):
                right = mid
            else:
                left = mid + 1
        return left



        