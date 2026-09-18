# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node, target1, target2):
            if not node:
                return

            #print(node.val)

            if node.val > target1 and node.val > target2:
                return dfs(node.left, target1, target2)
            elif node.val < target1 and node.val < target2:
                return dfs(node.right, target1, target2)
            else:
                return node

        return dfs(root, p.val, q.val)