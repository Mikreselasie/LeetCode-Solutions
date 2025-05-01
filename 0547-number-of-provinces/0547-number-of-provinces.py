from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])  # Path compression
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_j] = root_i  # Union

        for i in range(n):
            for j in range(i+1, n):  # Only upper triangle to avoid double-processing
                if isConnected[i][j] == 1:
                    union(i, j)

        # Count unique roots
        return len(set(find(i) for i in range(n)))
