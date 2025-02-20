class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        diff_arr = [0]*len(nums)

        for request in requests:
            diff_arr[request[0]] += 1
            if request[1] < len(nums)-1:
                diff_arr[request[1]+1] -= 1
        running = diff_arr[0]
        for i in range(1,len(diff_arr)):
            running += diff_arr[i]
            diff_arr[i] = running
        
        diff_arr.sort()
        nums.sort()
        print(diff_arr,nums)
        running = 0
        for i in range(len(nums)):
            running += diff_arr[i] * nums[i]
        return running%(10**9+7)
