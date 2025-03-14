# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def postorder(curr):
            if curr:
                postorder(curr.left)
                postorder(curr.right)
                answer.append(curr.val)
        postorder(root)
        return answer