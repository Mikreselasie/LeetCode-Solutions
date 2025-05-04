class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        my_dict = defaultdict(int)
        for i in range(1,7):
            for j in range(i,7):
                my_dict[(i,j)] = 0
        
        for a,b in dominoes:
            my_dict[(min(a,b),max(a,b))] += 1
        ans = 0
        for key,val in my_dict.items():
            if val>1:
                ans += math.comb(val,2)
        return ans
        