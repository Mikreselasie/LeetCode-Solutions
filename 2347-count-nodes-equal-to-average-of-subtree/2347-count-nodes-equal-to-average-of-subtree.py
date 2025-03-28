# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def post_order(root):
            nonlocal count
            if not root:
                return (0,0)
            left = post_order(root.left)
            right = post_order(root.right)
            total = left[0] + right[0] + root.val

            total_cnt = left[1] + right[1] + 1

            if total//total_cnt == root.val:
                count += 1 
            return (total,total_cnt)
        post_order(root)
        return count