class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        multiply_count = Counter()
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                multiply_count[nums[i]*nums[j]] += 1
        
        for p,c in multiply_count.items():
            count += ((c)*(c-1)//2)*8
        return count


                
        