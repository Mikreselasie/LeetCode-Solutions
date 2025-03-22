# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minValueNode(node):
            current = node
            # Find the leftmost leaf
            while current.left:
                current = current.left
            return current
        def deleteNode(root, key):
            # Return if the tree is empty
            if not root:
                return root
            # Find the node to be deleted
            if key < root.val:
                root.left = deleteNode(root.left, key)
            elif key > root.val:
                root.right = deleteNode(root.right, key)
            else:
            # If the node is with only one child or no child
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                # If the node has two children,
                # place the inorder successor in position of the node to be deleted
                temp = minValueNode(root.right)
                root.val = temp.val
                # Delete the inorder successor
                root.right = deleteNode(root.right, temp.val)
            return root

        return deleteNode(root,key)