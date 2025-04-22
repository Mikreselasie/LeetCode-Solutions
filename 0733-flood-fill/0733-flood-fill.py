class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        if starting == color:
            return image

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        def isValid(row, col):
            return (
                0 <= row < len(image)
                and 0 <= col < len(image[0])
                and (row, col) not in visited
                and image[row][col] == starting
            )

        def recur(row, col):
            if not isValid(row, col):
                return
            image[row][col] = color
            visited.add((row, col))

            for dr, dc in directions:
                recur(row + dr, col + dc)

        recur(sr, sc)
        return image
