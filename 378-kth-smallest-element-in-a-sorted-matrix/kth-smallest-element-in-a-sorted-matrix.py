class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def countLessOrEqual(matrix, target):
            n = len(matrix)
            count = 0
            row = n - 1
            columns = 0

            while row >= 0 and columns < n:
                if matrix[row][columns] <= target:
                    count += row + 1
                    columns += 1
                else:
                    row -= 1
            return count
        
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n - 1][n - 1]

        while left < right:
            mid = (left + right) // 2
            count = countLessOrEqual(matrix, mid)

            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left