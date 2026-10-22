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
        def dfs(node: TreeNode | None) -> int:
            if not node:
                return 0

            ret_val = node.val if low <= node.val <= high else 0

            if node.val > low:
                # the left may be in bounds
                ret_val += dfs(node.left)

            if node.val < high:
                # the right may be in bounds
                ret_val += dfs(node.right)

            return ret_val

        return dfs(root)