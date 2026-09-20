# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lowest = -2 ** 31
        highest = 2 ** 31 - 1

        def valid(node, low, high):
            if not node:
                return True

            if not(low <= node.val <= high):
                return False

            return valid(node.left, low, node.val - 1) and valid(node.right, node.val + 1, high)

        return valid(root, lowest, highest)