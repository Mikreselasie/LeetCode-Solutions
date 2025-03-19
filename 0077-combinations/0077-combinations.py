class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        temp = []
        def helper(m):
            temp.append(m)
            if len(temp) == k:
                ans.append(temp.copy())
                temp.pop()
                return 
            
            for i in range(m+1,n+1):
                helper(i)
            temp.pop()
        for i in range(1,n-k+2):
            helper(i)

        return ans
