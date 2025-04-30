class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = [[] for i in range(numCourses)]

        for key,val in prerequisites:
            adj_list[key].append(val)
        
        def dfs(curr,promised,visited):
            if curr == promised: return True
            if curr in visited: return False
            visited.add(curr)

            for num in adj_list[curr]:
                if dfs(num,promised,visited): return True
            return False
        
        ans = []
        for key,val in queries:
            visited = set()
            ans.append(dfs(key,val,visited))
        return ans