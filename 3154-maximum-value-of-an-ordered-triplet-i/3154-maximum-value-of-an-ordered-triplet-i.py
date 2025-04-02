class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_no = 0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    max_no = max(max_no,(nums[i]-nums[j])*nums[k])
        return max_no