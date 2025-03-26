# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        if not root:
            return []
        ans = []
        level = 0
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if level%2:
                ans.append(temp[::-1])
            else:
                ans.append(temp[:])
            level += 1
        return ans