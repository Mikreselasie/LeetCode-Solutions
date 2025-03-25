class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        first = -1
        def first_pos(left,right):
            nonlocal first
            while left <= right:
                mid = (left + right)//2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if nums[mid] == target:
                        first = mid
                    right = mid - 1
            return first
        last = -1
        def last_pos(left,right):
            nonlocal last
            while left <= right:
                mid = (left + right)//2
                if nums[mid] > target:
                    right = mid -1
                else:
                    if nums[mid] == target:
                        last = mid
                    left = mid + 1
            return last
        first,last = first_pos(left,right),last_pos(left,right)
        return [first,last]


            


                                     