class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        def isValid(row,col):
            return (0<=row<len(grid) and 0<=col<len(grid[0]) and grid[row][col] == 1 and (row,col) not in visited)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))
        
        cnt = 0
        while fresh > 0:
            if cnt > len(grid)*len(grid[0]): return -1
            for idx in range(len(rotten)):
                row,col = rotten.popleft()
                for dr,dc in directions:
                    if isValid(row+dr,col+dc):
                        fresh -= 1
                        rotten.append((row+dr,col+dc))
                        visited.add((row+dr,col+dc))
            cnt += 1
        return cnt




        