class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [nums2[0]]
        my_dict = dict()

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                num = stack.pop()
                my_dict[num] = nums2[i]
            stack.append(nums2[i])
        ans = []
        for numm in nums1:
            if numm in my_dict:
                ans.append(my_dict[numm])
            else:
                ans.append(-1)
        return ans



        