class NumArray:

    def __init__(self, nums: List[int]):
        self.my_arr = [0]*len(nums)
        for i in range(len(nums)):
            if i >0:
                self.my_arr[i] = self.my_arr[i-1] + nums[i]
            else:
                self.my_arr[i] = nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.my_arr[right]-self.my_arr[left-1]
        else:
            return self.my_arr[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)