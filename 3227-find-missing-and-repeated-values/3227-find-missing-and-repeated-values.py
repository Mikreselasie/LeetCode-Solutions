class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        my_count = Counter()
        n = len(grid)**2
        for row in grid:
            my_count.update(Counter(row))
        ans = []

        for key,val in my_count.items():
            if val == 2:
                ans.append(key)
                break
        ans.append((n*(n+1))//2 - sum(my_count.keys()))

        return ans
        
        
        
        