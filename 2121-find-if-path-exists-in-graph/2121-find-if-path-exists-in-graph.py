class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        to_ease = defaultdict(list)

        for num,num2 in edges:
            to_ease[num].append(num2)
            to_ease[num2].append(num)
        
        visited = set()
        def dfs(vertex):
            nonlocal visited
            visited.add(vertex)
            if vertex == destination:
                return True


            for neighbour in to_ease[vertex]:
                if neighbour not in visited:
                    ret = dfs(neighbour)
                    if ret:
                        return True
            return False
                
        return dfs(source)