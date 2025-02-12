class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        new_list = [[] for _ in range((len(mat) + len(mat[0]) - 1))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                new_list[i+j].append(mat[i][j])
        diagonal = []
        for idx in range(len(new_list)):
            if idx%2 == 0:
                diagonal.extend(reversed(new_list[idx]))
            else:
                diagonal.extend(new_list[idx])
        return diagonal
        
        
            
            

        