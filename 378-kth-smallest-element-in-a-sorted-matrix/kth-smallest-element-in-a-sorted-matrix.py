class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def smallerOrEqual(matrix, target):
            n = len(matrix)
            rows = n - 1
            count = 0
            columns = 0

            while rows >= 0 and columns < n:
                if matrix[rows][columns] <= target:
                    count += rows + 1
                    columns += 1
                else:
                    rows -= 1
            return count >= k
        n = len(matrix) 
        left = matrix[0][0]
        right = matrix[n - 1][n - 1]

        while left < right:
            mid = (left + right) // 2
            if smallerOrEqual(matrix, mid):
                right = mid
            else:
                left = mid + 1
        return left