class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_count = Counter(nums)

        sorted_count = sorted(num_count.items(),key = lambda item: item[1],reverse = True)

        if sorted_count[0][1] > 1:
            return True
        else:
            return False
        