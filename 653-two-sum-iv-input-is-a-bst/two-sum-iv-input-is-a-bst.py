# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodes = {}

        found = False
        
        def dfs(node):
            nonlocal found
            if not node:
                return

            dfs(node.left)

            complement = k - node.val
            if complement in nodes:
                found = True
                return

            nodes[node.val] = node

            dfs(node.right)

        dfs(root)
        return found