class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefix_max = [nums[0]]
        suffix_max = [nums[-1]]

        for num in nums[1:]:
            prefix_max.append(max(num,prefix_max[-1]))

        for num in nums[::-1]:
            suffix_max.append(max(suffix_max[-1],num))
        
        suffix_max = suffix_max[::-1]
        max_no = 0
        print(suffix_max,prefix_max)
        for i in range(1,len(nums)-1):
            max_no = max(max_no,(prefix_max[i]-nums[i])*suffix_max[i+1])
        return max_no
