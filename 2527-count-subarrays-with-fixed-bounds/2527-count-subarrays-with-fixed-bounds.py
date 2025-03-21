class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        left = 0
        e = -1
        s = -1
        for i in range(len(nums)):
            if nums[i]>maxK or nums[i]<minK:
                left=i+1
                e= -1
                s = -1
            if nums[i]==minK:
                s=i
            if nums[i]==maxK:
               e=i

            if e!=-1 and s!=-1:
                count+=max(min(s,e)-left+1,0)   
        return count      


