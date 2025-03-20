class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        pt = 0
        def backtrack(temp,arr,pt):
            
            for i in range(pt,len(candidates)):
                temp += candidates[i]
                arr.append(candidates[i])
                if temp < target:
                    backtrack(temp,arr,i)
                if temp == target:
                    ans.append(arr[:])
                temp -= candidates[i]
                arr.pop()
        backtrack(0,[],0)
        return ans