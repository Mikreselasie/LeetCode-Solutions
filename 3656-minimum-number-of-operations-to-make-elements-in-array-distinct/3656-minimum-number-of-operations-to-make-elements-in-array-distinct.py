class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        left = 0
        steps = 0
        
        counter = Counter(nums)
        print(sum(counter.values()))

        while len(counter) < sum(counter.values()):
            for i in range(left,min(left+3,len(nums))):
                counter[nums[i]] -= 1
                if counter[nums[i]] == 0:
                    del counter[nums[i]]
            steps += 1
            left += 3
        return steps

        