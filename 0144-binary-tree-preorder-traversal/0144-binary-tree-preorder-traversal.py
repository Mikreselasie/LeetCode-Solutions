# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    
        answer = []
        def preorder(curr):
            if curr:
                answer.append(curr.val)
                preorder(curr.left)
                preorder(curr.right)
        preorder(root)
        return answer