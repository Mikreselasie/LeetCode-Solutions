# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return 
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        half = len(nums)//2

        root = TreeNode(nums[half])
        root.left = self.sortedArrayToBST(nums[:half])
        root.right = self.sortedArrayToBST(nums[half + 1:])

        return root