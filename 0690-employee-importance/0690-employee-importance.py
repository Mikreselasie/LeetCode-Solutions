"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        data = defaultdict(list)
        for person in employees: 
            data[person.id] = (person.importance,person.subordinates)

        ans = 0
        def dfs(node):
            nonlocal ans
            ans += data[node][0]

            for num in data[node][1]:
                dfs(num)
        dfs(id)
        
        return ans
