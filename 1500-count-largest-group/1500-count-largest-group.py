class Solution:
    def countLargestGroup(self, n: int) -> int:
        nums = defaultdict(int)

        for i in range(1,n+1):
            toGroup = 0
            while i:
                toGroup += i%10
                i //= 10
            nums[toGroup] += 1
        
        maxi = max(nums.values())
        ans = 0
        for key,val in nums.items():
            if val == maxi: ans += 1
        return ans


        