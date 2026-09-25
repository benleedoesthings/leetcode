# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        found = False
        def dfs(node, path_sum):
            nonlocal found
            if not node:
                return

            path_sum += node.val
            #print("added", node.val)
            #print("sum is now", path_sum)

            if not node.left and not node.right and path_sum == targetSum:
                found = True
                return

            dfs(node.left, path_sum)
            dfs(node.right, path_sum)

        dfs(root, 0)

        return found