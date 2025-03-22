# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        temp_max = 0
        def bfs_tree(root):
            if not root:
                return max(queue)
            queue = deque([root])
            ans = []
            while queue:
                a = float("-inf")
                level = len(queue)

                for _ in range(level):
                    node = queue.popleft()
                    a = max(a,node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                ans.append(a)
            return ans
        return bfs_tree(root)