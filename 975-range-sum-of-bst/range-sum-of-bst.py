# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        # I love binary search trees
        # I love binary search trees
        # If I repeat this enough I will solve this problem
        if not root:
            return 0

        ret_val = root.val if low <= root.val <= high else 0

        if root.val > low:
            # the left subtree may be in bounds
            ret_val += self.rangeSumBST(root.left, low, high)

        if root.val < high:
            # the right subtree may be in bounds
            ret_val += self.rangeSumBST(root.right, low, high)

        return ret_val
