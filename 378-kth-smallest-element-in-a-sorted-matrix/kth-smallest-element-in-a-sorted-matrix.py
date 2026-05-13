class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def count_less_or_equal(matrix, target):
            count = 0
            n = len(matrix)
            row = n - 1
            column = 0


            while row >= 0 and column < n:
                if matrix[row][column] <= target:
                    count += row + 1
                    column += 1
                else:
                    row -= 1
            return count

        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n-1][n-1]

        while left < right:
            mid = (left + right) // 2
            count = count_less_or_equal(matrix, mid)
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left

