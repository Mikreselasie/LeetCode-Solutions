class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        p = 0
        for i in range(len(nums)):
            p = i
            if nums[i] >= 0:
                p = (p + nums[i] % len(nums)) % len(nums)
                result.append(nums[p])
            else:
                x = nums[i] * -1
                y = (x % len(nums)) * -1
                p += y 
                result.append(nums[p])
        return result

        