class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        dicit = Counter(blocks[:k])
        ans = dicit["W"]

        for i in range(k,len(blocks)):
            dicit[blocks[i-k]] -= 1
            dicit[blocks[i]] += 1
            ans = min(ans,dicit["W"])
            # print(dicit,ans)

        return ans
            

        