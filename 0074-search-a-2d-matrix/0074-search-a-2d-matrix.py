from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False  # Edge case: empty matrix
        
        row_left, row_right = 0, len(matrix) - 1
        col_left, col_right = 0, len(matrix[0]) - 1

        while row_left <= row_right and col_left <= col_right:
            mid_row = (row_left + row_right) // 2
            mid_col = (col_left + col_right) // 2

            if matrix[mid_row][mid_col] == target:
                return True

            elif matrix[mid_row][mid_col] > target:
                if matrix[mid_row][0] > target:
                    row_right = mid_row - 1 
                else:
                    col_right = mid_col - 1 
            else:  
                if matrix[mid_row][-1] < target:
                    row_left = mid_row + 1 
                else:
                    col_left = mid_col + 1
        return False  # Target not found
