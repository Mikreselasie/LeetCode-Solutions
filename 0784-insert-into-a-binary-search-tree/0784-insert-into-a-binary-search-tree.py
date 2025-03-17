# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def helper(root,val):
            if not root.left and val < root.val:
                root.left = TreeNode(val)
                return 
            if not root.right and val > root.val:
                root.right = TreeNode(val)
                return

            if root.val > val:
                helper(root.left,val)
            if root.val < val:
                helper(root.right,val)
        helper(root,val)
        return root