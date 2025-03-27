# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        num1 = 0
        ans = 0
        def helper(root):
            nonlocal ans
            nonlocal num1
            if not root:
                return
            num1 = num1*10 + root.val
            if not root.left and not root.right:
                ans += num1
            helper(root.left)
            helper(root.right)
            num1 //= 10

            return ans
        
        return helper(root)
