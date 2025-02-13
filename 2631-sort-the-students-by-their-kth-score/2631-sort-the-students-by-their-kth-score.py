class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        my_sort = sorted(score,key = lambda x: x[k],reverse = True)

        return my_sort
        