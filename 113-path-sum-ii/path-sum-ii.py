# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        ans = []

        def dfs(node, path, total):
            nonlocal ans

            if not node:
                return

            if not node.left and not node.right:
                if total + node.val == targetSum:
                    ans.append(path + [node.val])
                return

            dfs(node.left, path + [node.val], total + node.val)
            dfs(node.right, path + [node.val], total + node.val)
            
        dfs(root, [], 0)

        return ans