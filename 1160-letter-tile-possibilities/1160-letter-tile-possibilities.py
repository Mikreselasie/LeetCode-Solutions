class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)  # Count occurrences of each letter
        
        def backtrack():
            total = 0
            for tile in count:
                if count[tile] > 0:
                    count[tile] -= 1  # Choose this tile
                    total += 1 + backtrack()  # 1 for the current choice
                    count[tile] += 1  # Undo the choice (backtrack)
            return total
        
        return backtrack()
