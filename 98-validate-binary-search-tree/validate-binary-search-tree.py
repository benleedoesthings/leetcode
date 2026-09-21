# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True
        last_val = -2 ** 31 - 1
        def inorder(node):
            nonlocal valid
            nonlocal last_val

            if not node:
                return

            inorder(node.left)

            if last_val >= node.val:
                valid = False
                return

            last_val = node.val

            inorder(node.right)

        inorder(root)
        return valid