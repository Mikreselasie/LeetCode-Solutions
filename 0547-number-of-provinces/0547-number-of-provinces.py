class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_mtrx = defaultdict(list)
        n = len(isConnected)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj_mtrx[i].append(j)
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for val in adj_mtrx[node]:
                if node != val:
                    dfs(val)
        cnt = 0
        for num in range(n):
            if num not in visited:
                cnt += 1
                dfs(num)
        return cnt

        