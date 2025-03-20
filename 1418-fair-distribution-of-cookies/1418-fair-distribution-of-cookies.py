class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k == len(cookies): return max(cookies)
        bucket = [0]*k
        fairness = 1000000
        def fair(bucket,i):
            nonlocal fairness
            if i == len(cookies):
                fairness = min(fairness,max(bucket))
                return 

            for l in range(k):
                bucket[l] += cookies[i]
                fair(bucket,i+1)
                bucket[l] -= cookies[i]

        fair(bucket,0)
        return fairness