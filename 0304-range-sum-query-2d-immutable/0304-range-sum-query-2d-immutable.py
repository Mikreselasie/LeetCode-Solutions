from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_matrix = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            running_row_sum = 0
            for col in range(cols):
                running_row_sum += matrix[row][col]
                self.prefix_matrix[row][col] = running_row_sum
                if row > 0:
                    self.prefix_matrix[row][col] += self.prefix_matrix[row - 1][col]
        print(self.prefix_matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix_matrix[row2][col2]
        above = self.prefix_matrix[row1 - 1][col2] if row1 > 0 else 0
        left = self.prefix_matrix[row2][col1 - 1] if col1 > 0 else 0
        overlap = self.prefix_matrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return total - above - left + overlap
