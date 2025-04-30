class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = dict()
        ans = []

        def dfs(i):
            if i in visited: return visited[i]
            visited[i] = False

            for neigh in graph[i]:
                if not dfs(neigh): 
                    return visited[i]
            visited[i] = True
            return visited[i]

        for i in range(n):
            if dfs(i):
                ans.append(i)
            
        return ans