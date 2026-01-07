# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ans = 0
        MOD = 10**9 + 7

        def bfs(root):
            total = 0
            queue = deque([root])

            while queue:
                temp = queue.popleft()
                if temp:
                    total += temp.val
                
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            return total
        total = bfs(root)

        def dfs(node):
            nonlocal ans

            if not node:
                return 0
            
            temp = dfs(node.left) + dfs(node.right) + node.val

            difference = total - temp
            ans = max(ans, (difference*temp))

            return temp

        dfs(root)
        return ans % MOD      

        