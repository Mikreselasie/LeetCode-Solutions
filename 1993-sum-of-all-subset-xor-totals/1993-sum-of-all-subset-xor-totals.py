class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        store = []
        def subset_generator(idx,found,store):
            if idx == len(nums):
                store.append(found[:])
                return
            found.append(nums[idx])
            subset_generator(idx+1,found,store)

            found.pop()
            subset_generator(idx+1,found,store)

        subset_generator(0,[],store)
        ans = 0

        for nums in store:
            temp = 0
            for num in nums:
                temp ^= num
            ans += temp
        return ans
            
