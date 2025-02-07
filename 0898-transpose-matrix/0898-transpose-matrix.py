class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = []
        down = 0 
        right = 0
        while right < len(matrix[0]):
            temp_list = []
            down = 0
            while down < len(matrix):
                temp_list.append(matrix[down][right])
                down += 1
            new_matrix.append(temp_list)
            right += 1
        return new_matrix
