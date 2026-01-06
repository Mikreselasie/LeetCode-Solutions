# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        
        def level_order_sum(root):
            if root is None:
                return []

            max_sum = float("-inf")
            level = 1
            ans_level = level
            queue = deque([root])

            while queue:
                # 1. Snapshot the size of the queue. 
                # This is the number of nodes at the current level.
                level_size = len(queue)
                current_level_sum = 0
                
                # 2. Iterate ONLY through nodes of the current level
                for _ in range(level_size):
                    node = queue.popleft()
                    current_level_sum += node.val
                    
                    # Add children for the NEXT level
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                
                # 3. Store the sum for this level
                if current_level_sum > max_sum:
                    ans_level = level
                    max_sum = current_level_sum
                level += 1

            return ans_level
        return level_order_sum(root)

        