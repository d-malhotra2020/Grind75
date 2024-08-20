class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        
        top = 0
        bottom = rows - 1
        
        while (top <= bottom):
            row = (top + bottom)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        if not (top <= bottom):
            return False
        
        left = 0 
        right = columns - 1
        row = (top + bottom)//2
        while (left <= right):
            mid = (left + right)//2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False