class Solution:
    def minOperations(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        n = len(nums)
        ones = nums.count(1)
        if ones: return n - ones
        res = "inf"
        for i in range(n):
            # subarray starting from i
            g = nums[i]
            # try each element after i
            for j in range(i + 1, n):
                # to calculate gcd
                g = gcd(g, nums[j])
                # if the gcd is 1
                if g == 1:
                    # then we calculate the min ops
                    res = min(res, j - i)
        # no result -> return -1
        if res == "inf": return -1
        # otherwise, return res + n - 1
        # i.e. the min ops to turn the shortest subarray to 1 + 
        #      use that 1 to convert n - 1 elements to 1
        return res + n - 1