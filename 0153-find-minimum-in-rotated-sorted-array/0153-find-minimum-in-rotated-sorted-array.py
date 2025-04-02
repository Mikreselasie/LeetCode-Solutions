class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        ans = nums[0]
        while left <= right:
            mid = (left+right)//2
            print(nums[left],nums[right],nums[mid])
            if nums[mid] <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1
            ans = min(ans,nums[mid])
        return ans