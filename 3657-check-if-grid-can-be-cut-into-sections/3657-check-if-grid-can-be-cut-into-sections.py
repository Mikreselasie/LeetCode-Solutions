class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        horizontals = []
        verticals = []

        for rectangle in rectangles:
            horizontals.append([rectangle[0],rectangle[2]])
            verticals.append([rectangle[1],rectangle[3]])
        
        horizontals.sort()
        verticals.sort()
        prev = 0
        cnt = 0

        for hor in horizontals:
            if prev <= hor[0]:
                cnt += 1
            prev = max(prev,hor[1])
        
        if cnt > 2:
            return True
        
        prev = 0
        cnt = 0
        
        for ver in verticals:
            if prev <= ver[0]:
                cnt += 1
            prev = max(prev,ver[1])
        
        if cnt > 2:
            return True

        return False