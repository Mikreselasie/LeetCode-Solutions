class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        temp = defaultdict(int)
        if not edges:
            return 0 if n== 1 else -1

        for win,lose in edges:
            temp[win] += 0
            temp[lose] += 1
        if len(temp) < n: return -1
        cnt = 0
        ans = -1
        
        for key,val in temp.items():
            if val == 0: 
                cnt += 1
                ans = key
            if cnt > 1: return -1
        return ans


        