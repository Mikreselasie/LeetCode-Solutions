class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        end = n * n
        curr = 1
        moves = 0

        def get_coordinates(pos):
            r = (pos - 1) // n
            c = (pos - 1) % n
            row = n - 1 - r
            col = c if r % 2 == 0 else n - 1 - c
            return row, col

        visited = set()
        from collections import deque
        queue = deque([(1, 0)])
        visited.add(1)

        while queue:
            curr, moves = queue.popleft()
            if curr == end:
                return moves
            for i in range(1, 7):
                next_pos = curr + i
                if next_pos > end:
                    continue
                row, col = get_coordinates(next_pos)
                if board[row][col] != -1:
                    next_pos = board[row][col]
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))
        return -1
