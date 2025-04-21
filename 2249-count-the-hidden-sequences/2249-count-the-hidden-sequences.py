class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        gap = upper - lower + 1
        new = [0]

        for num in differences:
            new.append(new[-1]+num)
        
        maxi = max(new)
        mini = min(new)

        ranges = maxi - mini
        
        return max(0,gap - ranges)
        