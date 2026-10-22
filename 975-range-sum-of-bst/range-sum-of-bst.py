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
        ans = 0

        def dfs(node: TreeNode | None):
            nonlocal ans
            if not node:
                return

            if low <= node.val <= high:
                ans += node.val

            if node.val > low:
                # the left may be in bounds
                dfs(node.left)

            if node.val < high:
                # the right may be in bounds
                dfs(node.right)


        dfs(root)
        return ans