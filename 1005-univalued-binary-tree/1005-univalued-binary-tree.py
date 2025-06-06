# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue =  deque([root])
        val = root.val
        while queue:
            node = queue.popleft()
            if node and node.val != val: return False
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return True
        