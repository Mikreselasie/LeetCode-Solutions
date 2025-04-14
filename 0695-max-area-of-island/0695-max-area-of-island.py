class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        maxArea = 0

        def isValid(newRow, newCol):
            return (
                0 <= newRow < len(grid)
                and 0 <= newCol < len(grid[0])
                and grid[newRow][newCol] == 1
                and (newRow, newCol) not in visited
            )

        visited = set()

        def dfs(newRow, newCol):
            visited.add((newRow, newCol))
            area = 1
            for dr, dc in directions:
                tempRow, tempCol = newRow + dr, newCol + dc
                if isValid(tempRow, tempCol):
                    area += dfs(tempRow, tempCol)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if isValid(i, j):
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea
