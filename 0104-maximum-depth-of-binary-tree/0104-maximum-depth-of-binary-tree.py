# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        my_count = 0
        def helper(my_count,root):
            if not root:
                return 0
            my_count = max(my_count,1 + helper(my_count,root.left),1 +helper(my_count,root.right))
            return my_count
        return helper(my_count,root)