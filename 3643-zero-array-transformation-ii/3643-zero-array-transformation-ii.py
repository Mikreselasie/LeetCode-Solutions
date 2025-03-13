class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        ptr = 0
        running = 0
        if sum(nums) == 0:
            return 0
        diff_arr = [0]*len(nums)
        vals = []
        for idx,query in enumerate(queries):
            diff_arr[query[0]] += query[2]
            if query[1] + 1 < len(nums):
                diff_arr[query[1] + 1] -= query[2]

            if query[0] <= ptr <= query[1]:
                running += query[2]
            while ptr < len(nums) and running >= nums[ptr]:
                ptr += 1
                if ptr == len(nums):
                    return idx + 1
                running += diff_arr[ptr]
        return -1
            