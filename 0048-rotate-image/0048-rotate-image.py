class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        j = 0
        for i in list(zip(*matrix[::-1])):
            matrix[j] = i
            j +=1
        