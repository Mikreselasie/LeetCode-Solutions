# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node,min_no,max_no):
            if not node:
                return float("-inf")
            min_no = min(min_no,node.val)
            max_no = max(max_no,node.val)

            left = helper(node.left,min_no,max_no)
            right = helper(node.right,min_no,max_no)

            return max(max_no - min_no, max(left,right))
        return helper(root,float("inf"),float("-inf"))
            