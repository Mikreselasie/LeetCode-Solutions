class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [1]*len(nums)
        prefix = [1]*len(nums)
        answer = []
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
            suffix[len(nums)-i-1] = suffix[len(nums)-i] * nums[len(nums)-i]
        for i in range(len(nums)):
            answer.append(prefix[i]*suffix[i])
        return answer

        