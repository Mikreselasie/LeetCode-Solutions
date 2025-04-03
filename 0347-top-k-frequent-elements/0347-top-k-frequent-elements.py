class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums)

        buckets = [[] for i in range(max(counted.values()))]

        for num,cnt in counted.items():
            buckets[cnt-1].append(num)
        
        ans = []
        ptr = len(buckets)-1
        while k>0:
            ans.extend(buckets[ptr])
            k -= len(buckets[ptr])
            ptr -= 1
        return ans

