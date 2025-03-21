class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
      return [list(sub) for sub in permutations(nums,len(nums))]  