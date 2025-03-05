class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            for i in range(len(nums2)):
                if nums2[i] == num:
                    pt = i
                    while pt < len(nums2) and nums2[pt] <= nums2[i]:
                        pt += 1
                    if pt == len(nums2):
                        ans.append(-1)
                    else:
                        ans.append(nums2[pt])
                    break
        return ans
                        
        