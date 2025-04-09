class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for num in nums:
            if num < k: return -1
        
        counter = Counter(nums)

        new = []
        for num,val in counter.items():
            new.append((num,val))
        
        new.sort()
        for i in range(len(new)):
            if new[i][0] == k:
                return len(new) - (i+1)
        return len(new)